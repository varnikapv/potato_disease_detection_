import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load trained model
model = tf.keras.models.load_model('potato_disease_model.h5')

# Class labels
classes = ['Early_Blight', 'Healthy', 'Late_Blight']

# Streamlit UI
st.title("🥔 Potato Disease Detection")
st.write("Upload a potato leaf image and the model will predict its condition.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Leaf', use_container_width=False, width=300)


    # Preprocess image
    img = img.resize((128,128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Prediction
    prediction = model.predict(img_array)
    predicted_class = classes[np.argmax(prediction)]

    st.success(f"🍀 Predicted Class: {predicted_class}")
