import streamlit as st
import numpy as np
import cv2
from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="Erase Object", layout="wide")
st.title("EraseX")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Open image as PIL Image (keep for background_image)
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)
    st.image(image_np, caption="Original Image", use_container_width=True)  # use_container_width instead of deprecated

    st.markdown("**Draw over the object you want to remove:**")

    # Use PIL Image directly for background_image
    canvas_result = st_canvas(
        fill_color="rgba(255, 0, 0, 0.3)",
        stroke_width=35,
        stroke_color="white",
        background_image=image,  # PIL Image
        update_streamlit=True,
        height=image_np.shape[0],
        width=image_np.shape[1],
        drawing_mode="freedraw",
        key="canvas",
    )

    if st.button("Remove Object"):
        if canvas_result.image_data is not None:
            # Convert canvas to mask (RGBA → Gray → uint8)
            mask = canvas_result.image_data.astype(np.uint8)
            mask = cv2.cvtColor(mask, cv2.COLOR_RGBA2GRAY)
            _, mask = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY)

            mask = np.clip(mask, 0, 255).astype(np.uint8)

            # Dilate and blur mask for smooth inpainting
            kernel = np.ones((40, 40), np.uint8)
            mask = cv2.dilate(mask, kernel, iterations=1)
            mask = cv2.GaussianBlur(mask, (41, 41), 0)

            # Inpaint using Navier-Stokes
            result = cv2.inpaint(image_np, mask, 8, cv2.INPAINT_NS)

            st.image(result, caption="Object Removed", use_container_width=True)
        else:
            st.warning("Draw over the object first!")





















  





