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

# App header
st.title("🌱 AgriAI: Crop Disease & Yield Protection")
st.markdown("Upload a photo of a crop leaf below to detect potential diseases instantly and protect your harvest.")

# Load the trained model safely
@st.cache_resource
def load_my_model():
    return load_model('crop_disease_model.h5')

with st.spinner('Loading AI Model... Please wait!'):
    model = load_my_model()

# Expanded database for diseases with robust fallbacks
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

# File uploader widget
uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Crop Leaf', use_container_width=True)

    # Use session state so results persist on screen right after clicking analyze
    if "analyzed" not in st.session_state:
        st.session_state.analyzed = False
    if "pred_class" not in st.session_state:
        st.session_state.pred_class = ""
    if "conf" not in st.session_state:
        st.session_state.conf = 0.0

    if st.button('Analyze Leaf'):
        with st.spinner('Analyzing image for diseases...'):
            img_resized = image.resize((160, 160))
            img_array = tf.keras.utils.img_to_array(img_resized)
            img_array = tf.expand_dims(img_array, 0)

            predictions = model.predict(img_array)
            score = tf.nn.softmax(predictions[0])

            st.session_state.pred_class = class_names[np.argmax(score)]
            st.session_state.conf = 100 * np.max(score)
            st.session_state.analyzed = True

    # Render results automatically if analysis has been performed
    if st.session_state.analyzed:
        predicted_class = st.session_state.pred_class
        confidence = st.session_state.conf

        formatted_name = predicted_class.replace('_', ' - ').replace('_', ' ')
        st.success(f"Prediction: {formatted_name}")
# Look up details in DISEASE_INFO using the raw predicted_class
if predicted_class in DISEASE_INFO:
    info = DISEASE_INFO[predicted_class]
    
    st.markdown(f"### Severity: {info.get('severity', 'N/A')}")
    st.markdown(f"Description: {info.get('description', 'N/A')}")
    st.markdown(f"Management/Cure: {info.get('management', 'N/A')}")
    st.markdown(f"Prevention: {info.get('prevention', 'N/A')}")
else:
    st.info(f"Detailed info missing for key: {predicted_class}")
