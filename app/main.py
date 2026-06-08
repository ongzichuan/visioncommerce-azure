import streamlit as st
from PIL import Image

from services.storage_service import upload_image
from services.vision_service import analyse_image
from services.openai_service import generate_listing
from services.scoring_service import calculate_quality_score
from services.background_service import remove_background

if uploaded_file:

    image = Image.open(uploaded_file)
    image_bytes = uploaded_file.getvalue()

    background_removed = remove_background(
        image_bytes
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

    with col2:

        st.subheader("Background Removed")

        st.image(
            background_removed,
            use_container_width=True
        )