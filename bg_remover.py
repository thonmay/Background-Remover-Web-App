import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

# setting the window
st.set_page_config(
    layout="wide", page_title="Background Removal App", page_icon="🎨"
)

st.write("Remove Background from your Image")
st.sidebar.write("Upload & Download your image :gear:")

MAX_FILE_SIZE = 10 * 1024 * 1024    # 10 MB

col1, col2 = st.columns(2)

# for uploading image
upload = st.sidebar.file_uploader("Upload your image", type=["png", "jpg", "jpeg"]) 

def convert_img(img_file):
    """
    Convert PIL Image to bytes
    """
    buf = BytesIO()
    img_file.save(buf, format="PNG")
    bytes_img = buf.getvalue()
    return bytes_img

def remove_bg(upload):
    """
    Remove background from uploaded image
    """
    try:
        img = Image.open(upload)
        
        col1.write("Original Image")
        col1.image(img)
        
        fixed_img = remove(img)
        
        col2.write("Background Removed Image")
        col2.image(fixed_img)
        st.sidebar.markdown("\n")
        st.sidebar.download_button(
            "Download Background Removed Image",
            convert_img(fixed_img),
            "background_removed_image.png",
            "image/png"
        )
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Main logic
if upload is not None:
    if upload.size > MAX_FILE_SIZE:
        st.error("File size exceeds the maximum limit of 10 MB. Please upload a smaller file.")
    else:
        remove_bg(upload)
else:
    # When no file is uploaded
    st.info("Please upload an image to remove its background.")