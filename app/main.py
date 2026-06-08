import streamlit as st
from PIL import Image
from io import BytesIO

from services.storage_service import upload_image
from services.vision_service import analyse_image
from services.openai_service import generate_listing
from services.scoring_service import calculate_quality_score
from services.background_service import remove_background

st.set_page_config(
    page_title="VisionCommerce Azure",
    page_icon="🛒",
    layout="wide"
)

with st.sidebar:
    st.header("Platform Information")

    st.info("""
Technology Stack

• Azure AI Vision
• Azure Blob Storage
• Azure Container Apps
• Azure Container Registry
• Streamlit
• Docker
• Background Removal
""")

    st.success("System Status: Online")

st.title("VisionCommerce")

st.markdown("""
### AI-Powered E-Commerce Image Optimisation Platform

Analyse product images, detect quality issues, generate metadata and prepare marketplace-ready listings using Azure AI.

### Features

✅ Azure AI Vision

✅ Azure Blob Storage

✅ Background Removal

✅ Product Recognition

✅ Quality Assessment

✅ AI Listing Generation

✅ Cloud Hosted on Azure
""")

uploaded_file = st.file_uploader(
    "Upload Product Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    image_bytes = uploaded_file.getvalue()

    with st.spinner("Removing background..."):
        background_removed = image

    background_removed_image = Image.open(
        BytesIO(background_removed)
    )

    blob_url = upload_image(
        uploaded_file.name,
        image_bytes
    )

    with st.spinner("Analysing image with Azure AI Vision..."):
        analysis = analyse_image(
            image_bytes
        )

    quality_score = calculate_quality_score(
        analysis["tags"]
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Product Image")

        st.image(
            image,
            use_container_width=True
        )

        st.success(
            "Image successfully stored in Azure Blob Storage"
        )

        st.subheader("Background Removed")

        st.image(
            background_removed_image,
            use_container_width=True
        )

        st.download_button(
            label="Download Transparent PNG",
            data=background_removed,
            file_name="product_no_bg.png",
            mime="image/png"
        )

    with col2:
        st.subheader(
            "Azure AI Vision Analysis"
        )

        st.metric(
            "Quality Score",
            f"{quality_score}%"
        )

        st.write("Caption:")
        st.write(
            analysis["caption"]
        )

        st.write("Tags:")

        for tag in analysis["tags"]:
            st.write(
                f"- {tag}"
            )

    st.divider()

    st.subheader(
        "Product Details"
    )

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

    if st.button(
        "Generate Listing"
    ):
        if not product_name:
            st.warning(
                "Please enter a product name."
            )
        else:
            listing = generate_listing(
                product_name,
                category,
                analysis
            )

            st.subheader(
                "Generated Product Listing"
            )

            st.text_area(
                "AI Generated Listing",
                listing,
                height=350
            )