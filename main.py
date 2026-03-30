import cv2
import easyocr
import re # Naya module regex ke liye add kiya hai

image_path = r"C:\Users\Rajesh-Sharma\OneDrive\Desktop\cv_project\kyc_env\sample_id.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Error: Image load nahi hui. Path check karo.")
else:
    print("Process start ho rahi hai, please wait...\n")
    reader = easyocr.Reader(['en']) 
    result = reader.readtext(img)
    
    # Raw data ko ek list me store karenge
    extracted_texts = []
    for (bbox, text, prob) in result:
        if prob > 0.3:
            extracted_texts.append(text)

    # Variables jisme hum final clean data store karenge
    student_name = "Not Found"
    reg_number = "Not Found"

    # Data Parsing Logic
    for text in extracted_texts:
        # 1. Data Cleaning: Faltu ke symbols hatana
        clean_text = text.replace(';', '').strip()

        # 2. Registration Number Extract karna
        # Pattern check: 2 digits (\d{2}), 3 uppercase letters ([A-Z]{3}), 5 digits (\d{5})
        if re.search(r'\d{2}[A-Z]{3}\d{5}', clean_text):
            reg_number = clean_text
            
        # 3. Name Extract karna
        # Logic: Agar text uppercase me hai, length 6 se badi hai, aur college ka naam nahi hai
        elif clean_text.isupper() and len(clean_text) > 6 and "VIT" not in clean_text and "BHOPAL" not in clean_text:
            student_name = clean_text

    print("--- Final Cleaned Output ---")
    print(f"Name                : {student_name}")
    print(f"Registration Number : {reg_number}")