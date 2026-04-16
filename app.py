import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("best_model.h5")

st.title("Bird vs Drone Classifier")

file = st.file_uploader("Upload Image")

if file:
    img = Image.open(file).resize((224,224))
    st.image(img)

    img = np.array(img)/255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)

    if pred > 0.5:
        st.write("Drone Detected")
    else:
        st.write("Bird Detected")
