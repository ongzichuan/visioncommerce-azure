import streamlit as st
from PIL import Image

from services.storage_service import upload_image
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
    image_bytes = uploaded_file.getvalue()

    blob_url = upload_image(uploaded_file.name, image_bytes)

    with st.spinner("Analysing image with Azure AI Vision..."):
        analysis = analyse_image(image_bytes)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Product Image")
        st.image(image, use_container_width=True)
        st.success("Image uploaded to Azure Blob Storage")
        st.success("Image successfully stored in Azure Blob Storage")

    with col2:
        st.subheader("Azure AI Vision Analysis")
        st.write("**Caption:**")
        st.write(analysis["caption"])

        st.write("**Tags:**")
        for tag in analysis["tags"]:
            st.write(f"- {tag}")

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
            listing = generate_listing(
                product_name,
                category,
                analysis
            )

            st.subheader("Generated Product Listing")
            st.text_area(
                "AI Generated Listing",
                listing,
                height=350
            )