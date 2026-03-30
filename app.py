import streamlit as st
import cv2
import easyocr
import re
import numpy as np
import pandas as pd
from PIL import Image

# --- PAGE SETUP ---
st.set_page_config(page_title="KYC Vision Pro", page_icon="🪪", layout="wide")

# --- ADVANCED PREMIUM CSS ---
# Ye CSS aapke app ko ek modern dashboard ka look degi
st.markdown("""
<style>
    /* App ka background thoda aur deep aur clean kiya hai */
    .stApp {
        background-color: #0b0f19;
    }
    
    /* Top Header (Gradient Banner) */
    .hero-banner {
        background: linear-gradient(135deg, #4F46E5 0%, #EC4899 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 40px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    .hero-banner h1 {
        margin: 0;
        font-weight: 900;
        font-size: 3rem;
        letter-spacing: 1px;
    }
    .hero-banner p {
        margin: 10px 0 0 0;
        font-size: 1.2rem;
        opacity: 0.9;
    }

    /* Custom Result Cards */
    .data-card {
        background-color: #171c28;
        border: 1px solid #2a3143;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 6px solid #4F46E5;
        transition: all 0.3s ease;
    }
    .data-card:hover {
        transform: translateY(-5px);
        border-left: 6px solid #EC4899;
        box-shadow: 0 8px 15px rgba(236, 72, 153, 0.2);
    }
    .card-label {
        color: #94a3b8;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 8px;
        font-weight: 600;
    }
    .card-value {
        color: #ffffff;
        font-size: 1.8rem;
        font-weight: 700;
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- HERO BANNER (Header) ---
st.markdown("""
<div class="hero-banner">
    <h1>🪪 KYC Vision Pro</h1>
    <p>Next-Gen Identity Extraction using Deep Learning & OCR</p>
</div>
""", unsafe_allow_html=True)

# --- MODEL LOADING ---
@st.cache_resource(show_spinner=False)
def load_model():
    return easyocr.Reader(['en'])

reader = load_model()

# --- MAIN LAYOUT SECTION ---
# Layout ko thoda aur space diya hai taaki congested na lage
st.markdown("<br>", unsafe_allow_html=True)
col_upload, spacer, col_result = st.columns([1.2, 0.2, 1.5])

with col_upload:
    st.markdown("### 📄 1. Upload ID Document")
    st.markdown('<p style="color:#94a3b8; font-size:0.9rem;">Accepted formats: JPG, PNG. High resolution images give better accuracy.</p>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.markdown("<br>", unsafe_allow_html=True)
        # Image par ek clean border lagane ke liye st.image use kar rahe hain
        st.image(image, caption="Document Preview", use_container_width=True)

with col_result:
    st.markdown("### ⚡ 2. Extracted Intelligence")
    
    if uploaded_file is not None:
        with st.spinner("🤖 Neural Networks are scanning your document..."):
            img_array = np.array(image)
            img_cv2 = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
            
            result = reader.readtext(img_cv2)
            extracted_texts = [text for (bbox, text, prob) in result if prob > 0.3]
                
            student_name = "Not Detected"
            reg_number = "Not Detected"
            
            for text in extracted_texts:
                clean_text = text.replace(';', '').strip()
                
                # Reg Number Logic
                if re.search(r'\d{2}[A-Z]{3}\d{5}', clean_text):
                    reg_number = clean_text
                    
                # Name Logic
                elif clean_text.isupper() and len(clean_text) > 6 and "VIT" not in clean_text and "BHOPAL" not in clean_text and "HOSTELLER" not in clean_text:
                    if student_name == "Not Detected": 
                        student_name = clean_text

        # --- CUSTOM HTML CARDS FOR DISPLAY ---
        st.markdown(f"""
        <div class="data-card">
            <div class="card-label">Full Name</div>
            <div class="card-value">{student_name}</div>
        </div>
        
        <div class="data-card">
            <div class="card-label">Registration Number</div>
            <div class="card-value">{reg_number}</div>
        </div>
        """, unsafe_allow_html=True)

        # --- EXPORT BUTTON ---
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 💾 3. Export Data")
        
        user_data = {"Name": [student_name], "Registration Number": [reg_number]}
        df = pd.DataFrame(user_data)
        csv = df.to_csv(index=False).encode('utf-8')
        
        st.download_button(
            label="Download Clean CSV Report",
            data=csv,
            file_name='kyc_extracted_data.csv',
            mime='text/csv',
            use_container_width=True,
            type="primary" # Makes the button stand out
        )

        with st.expander("🛠️ View Developer Raw Logs"):
            st.json(extracted_texts)
    else:
        # Default state waiting card
        st.markdown("""
        <div style="background-color: #171c28; border: 1px dashed #4F46E5; border-radius: 12px; padding: 40px; text-align: center; color: #94a3b8; margin-top: 20px;">
            <h3 style="margin-top:0;">No Image Uploaded</h3>
            <p>Please upload a document from the left panel to begin the extraction process.</p>
        </div>
        """, unsafe_allow_html=True)