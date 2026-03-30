<div align="center">

# 🪪 Smart KYC Vision Pro
**Next-Gen Identity Extraction System powered by Deep Learning & OCR**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

</div>

---

## ⚡ Overview
**Smart KYC Vision Pro** is an end-to-end Machine Learning web application designed to automate the extraction of critical data from College ID Cards and KYC documents. Built with a focus on accuracy and aesthetic user experience, this tool eliminates manual data entry by instantly scanning, filtering, and structuring identity data.

Perfect for hackathons, BYOP (Bring Your Own Project) events, and automated data processing pipelines.

## ✨ Key Features
- **🤖 Automated OCR:** Utilizes `EasyOCR` (Deep Learning-based) to accurately read text from complex image backgrounds.
- **🧠 Smart Parsing:** Employs advanced Regular Expressions (`Regex`) to intelligently identify and separate Student Names and Registration Numbers from raw text.
- **🎨 Premium Aesthetic UI:** Features a custom-styled, highly responsive dashboard built with Streamlit and injected HTML/CSS for a modern SaaS look.
- **💾 1-Click Export:** Instantly converts extracted structured data into a downloadable CSV report for database integration.

---

## 🛠️ Tech Stack
- **Language:** Python
- **Computer Vision:** OpenCV (`cv2`)
- **Optical Character Recognition:** EasyOCR
- **Data Manipulation:** Pandas, NumPy
- **Frontend / UI:** Streamlit (with Custom CSS styling)

  

---
## 🚀 Installation & Setup

Follow these instructions to get a local copy up and running smoothly.

### 📋 Prerequisites
Ensure you have the following installed on your local machine:
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

🛠️ Step-by-Step Guide
1. Clone the Repository
Open your terminal and run the following command to download the project:

Bash
git clone [https://github.com/YourUsername/KYC-Data-Extractor.git](https://github.com/YourUsername/KYC-Data-Extractor.git)
cd KYC-Data-Extractor


2. Set Up a Virtual Environment (Highly Recommended)
It's a best practice to isolate project dependencies. Create and activate a virtual environment:

Bash
 For Windows:
python -m venv kyc_env
kyc_env\Scripts\activate

 For macOS/Linux:
python3 -m venv kyc_env
source kyc_env/bin/activate



3. Install Dependencies
With your virtual environment active, install the required Machine Learning and UI libraries:

Bash
pip install streamlit opencv-python easyocr pandas numpy pillow
(💡 Note: The first-time installation of EasyOCR might take a few extra minutes as it downloads the PyTorch deep learning models.)

4. Launch the Application
Fire up the Streamlit server to view the dashboard:

Bash
streamlit run app.py''





