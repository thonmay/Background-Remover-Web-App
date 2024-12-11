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
![alt text](example/img1.png)
![alt text](example/img2.png)


## Installation

1. Clone the repository:

>>  git clone https://github.com/thonmay/background-removal-app.git

>>  cd background-removal-app

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