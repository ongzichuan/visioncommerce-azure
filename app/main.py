if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        use_container_width=True
    )

    st.success("Upload successful")