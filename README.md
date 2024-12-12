# Background Remover Web App 🎨
 
 A Streamlit web application that removes backgrounds from images using the rembg library. This tool allows to upload images and download them with transparent backgrounds.

## Features

- Simple and intuitive user interface
- Supports multiple image formats (PNG, JPG, JPEG)
- Real-time background removal
- Side-by-side comparison of original and processed images
- One-click download of processed images
- File size limit protection (10MB)

## Demo
<img width="1434" alt="Screenshot 2024-12-11 at 6 02 41 PM" src="https://github.com/user-attachments/assets/1edd4fec-a33e-40a1-9511-e8d303b6f4a9" />

<img width="1434" alt="Screenshot 2024-12-11 at 6 01 46 PM" src="https://github.com/user-attachments/assets/6c0600cf-5650-4d54-97fe-65b82acfde0b" />


## Installation

1. Clone the repository:

>>  git clone: https://github.com/thonmay/Background-Remover-Web-App

>>  cd Background-Remover-Web-App

2. Install the required dependencies:

>>  pip install -r requirements.txt

# Usage
1. Run the Streamlit app:
>> streamlit run bg_remover.py
2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)
3. Upload an image using the sidebar
4. Wait for the background removal process to complete
5. Download the processed image using the download button


# Dependencies
streamlit
rembg
Pillow
python-io
base64
