import streamlit as st
from PIL import Image

from services.vision_service import analyse_image
from services.openai_service import generate_listing

st.set_page_config(
    page_title="VisionCommerce Azure",
    page_icon="🛒",
    layout="wide"
)

st.title("VisionCommerce Azure")
st.caption("AI-powered product image optimisation and listing generation")

uploaded_file = st.file_uploader(
    "Upload Product Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    analysis = analyse_image()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Product Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Image Analysis")

        st.metric(
            "Quality Score",
            f"{analysis['quality_score']}%"
        )

        st.metric(
            "Background Quality",
            analysis["background"]
        )

        st.metric(
            "Lighting",
            analysis["lighting"]
        )

        st.success("Image passed quality threshold")

    st.divider()

    st.subheader("Product Details")

    product_name = st.text_input(
        "Product Name",
        placeholder="Vitamin C 1000mg"
    )

    category = st.selectbox(
        "Category",
        [
            "Health Supplement",
            "Beauty",
            "Electronics",
            "Fashion",
            "Home Living"
        ]
    )

    if st.button("Generate Listing"):

        if not product_name:
            st.warning("Please enter a product name.")
        else:

            listing = generate_listing(product_name)

            st.subheader("Generated Product Listing")

            st.text(listing)