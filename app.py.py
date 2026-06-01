import streamlit as st
from PIL import Image
from sklearn.cluster import KMeans
import numpy as np

# App title
st.title("Persi - A Creative Palette Assistant")

# Upload image
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

# Run when image uploaded
if uploaded_file:

    # Open image
    image = Image.open(uploaded_file)

    # Show uploaded image
    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    # Resize for faster processing
    image = image.resize((150, 150))

    # Convert image into array
    img_array = np.array(image)

    # Reshape array for KMeans
    img_array = img_array.reshape(-1, 3)

    # Find dominant colors
    kmeans = KMeans(n_clusters=5)

    kmeans.fit(img_array)

    # Get palette colors
    colors = kmeans.cluster_centers_.astype(int)

    # Palette section
    st.subheader("Detected Color Palette")

    # Create 5 columns
    cols = st.columns(5)

    # Display each color
    for i, color in enumerate(colors):

        # Convert RGB to HEX
        hex_color = '#%02x%02x%02x' % tuple(color)

        cols[i].markdown(
            f"""
            <div style="
                width:100px;
                height:100px;
                background-color:{hex_color};
                border-radius:10px;
                border:1px solid #ccc;
            ">
            </div>

            <p style="text-align:center;">
                {hex_color}
            </p>
            """,
            unsafe_allow_html=True
        )