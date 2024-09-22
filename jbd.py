import streamlit as st
from PIL import Image
import io
from streamlit_cropper import st_cropper

# Set page layout
st.set_page_config(layout="wide")
st.title("Image Upload, Crop and Process")

# Sidebar for image upload
uploaded_file = st.file_uploader("Upload an image to crop", type=["png", "jpg", "jpeg"])

# If the user uploads an image
if uploaded_file is not None:
    # Open the uploaded image
    img = Image.open(uploaded_file)

    # Display the cropping tool directly after upload
    st.sidebar.write("Adjust the crop box, then press the **Crop** button below.")

    # Real-time cropping
    cropped_img = st_cropper(img, realtime_update=True, box_color='#FF0000', aspect_ratio=None)

    # When the user clicks the "Crop" button
    if st.sidebar.button('Crop'):
        # Display the cropped image in the main content area
        st.image(cropped_img, caption="Cropped Image", use_column_width=True)

        # Optionally, save the cropped image and provide a download link
        buffer = io.BytesIO()
        cropped_img.save(buffer, format="PNG")
        byte_img = buffer.getvalue()
        st.download_button(
            label="Download Cropped Image",
            data=byte_img,
            file_name="cropped_image.png",
            mime="image/png"
        )
