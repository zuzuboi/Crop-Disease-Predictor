import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Page configuration
st.set_page_config(
    page_title="AgriAI: Crop Disease Predictor",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 AgriAI: Crop Disease & Yield Protection")
st.markdown("Upload a photo of a crop leaf below to detect potential diseases instantly and protect your harvest.")

@st.cache_resource
def load_my_model():
    return load_model('crop_disease_model.h5')

with st.spinner('Loading AI Model... Please wait!'):
    model = load_my_model()

DISEASE_INFO = {
    "TomatoSeptoria_leaf_spot": {
        "severity": "Moderate to High",
        "description": "A fungal disease that creates small circular spots with dark borders and grey centers on lower leaves.",
        "management": "Remove and destroy infected lower leaves immediately. Apply a broad-spectrum fungicide.",
        "prevention": "Avoid overhead watering to keep leaves dry and practice crop rotation."
    },
    "TomatoEarly_blight": {
        "severity": "High",
        "description": "Characterized by dark brown spots with concentric rings, often starting on older leaves.",
        "management": "Prune heavily infected branches to improve air circulation and treat with appropriate fungicides.",
        "prevention": "Use disease-resistant seeds, mulch heavily beneath plants, and space them properly."
    },
    "Corn_(maize)Common_rust_": {
        "severity": "Moderate",
        "description": "Fungal infection producing small, cinnamon-brown to dark brown pustules on both upper and lower leaf surfaces.",
        "management": "Apply foliar fungicides if disease pressure is high and plants are in critical growth stages.",
        "prevention": "Plant resistant corn hybrids and ensure proper field drainage and crop residue management."
    }
}

class_names = [
    'AppleApple_scab', 'Apple_Black_rot', 'Apple_Cedar_apple_rust', 'Applehealthy',
    'Blueberryhealthy', 'Cherry_(including_sour)Powdery_mildew', 'Cherry_(including_sour)healthy',
    'Corn_(maize)Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)Common_rust_',
    'Corn_(maize)Northern_Leaf_Blight', 'Corn_(maize)healthy', 'GrapeBlack_rot',
    'GrapeEsca_(Black_Measles)', 'GrapeLeaf_blight_(Isariopsis_Leaf_Spot)', 'Grapehealthy',
    'OrangeHaunglongbing_(citrus_greening)', 'PeachBacterial_spot', 'Peachhealthy',
    'Pepper,_bellBacterial_spot', 'Pepper,_bellhealthy', 'PotatoEarly_blight',
    'PotatoLate_blight', 'Potatohealthy', 'Raspberryhealthy', 'Soybeanhealthy',
    'SquashPowdery_mildew', 'StrawberryLeaf_scorch', 'Strawberryhealthy',
    'TomatoBacterial_spot', 'TomatoEarly_blight', 'TomatoLate_blight', 'TomatoLeaf_Mold',
    'TomatoSeptoria_leaf_spot', 'TomatoSpider_mites Two-spotted_spider_mites',
    'TomatoTarget_Spot', 'TomatoYellow_Leaf_Curl_Virus', 'Tomatomosaic_virus', 'Tomatohealthy'
]

uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Crop Leaf', use_container_width=True)

    # Everything is nested properly inside this button execution block now
    if st.button('Analyze Leaf'):
        with st.spinner('Analyzing image for diseases...'):
            img_resized = image.resize((160, 160))
            img_array = tf.keras.utils.img_to_array(img_resized)
            img_array = tf.expand_dims(img_array, 0)

            predictions = model.predict(img_array)
            score = tf.nn.softmax(predictions[0])

            pred_idx = np.argmax(score)
            predicted_class = class_names[pred_idx]
            confidence = 100 * np.max(score)

        formatted_name = predicted_class.replace('_', ' ').strip('-')
        st.success(f"Prediction: {formatted_name}")
        st.info(f"Confidence Score: {confidence:.2f}%")

        if predicted_class in DISEASE_INFO:
            info = DISEASE_INFO[predicted_class]
            severity_risk = info['severity']
