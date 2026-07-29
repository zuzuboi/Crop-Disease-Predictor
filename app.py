import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Page configuration
st.set_page_config(
    page_title="AgriAI: Crop Disease Predictor",
    page_icon="🌿",
    layout="centered"
)

# App header
st.title("🌿 AgriAI: Crop Disease & Yield Protection")
st.markdown("Upload a photo of a crop leaf below to detect potential diseases instantly and protect your harvest.")

# Load the trained model (cached so it loads fast)
@st.cache_resource
def load_my_model():
    model = load_model('crop_disease_model.h5')
    return model

with st.spinner('Loading AI Model... Please wait!'):
    model = load_my_model()

# List of 38 PlantVillage class names matching your training order
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
    'OrangeHaunglongbing_(Citrus_greening)', 'PeachBacterial_spot', 'Peachhealthy',
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
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Crop Leaf', use_container_width=True)
    
    # Predict button
    if st.button('Analyze Leaf'):
        with st.spinner('Analyzing image for diseases...'):
            # Preprocess the image to match model expectations
            image = image.resize((160, 160))
            img_array = tf.keras.utils.img_to_array(image)
            img_array = tf.expand_dims(img_array, 0) # Create a batch
            
            # Make prediction
            predictions = model.predict(img_array)
            score = tf.nn.softmax(predictions[0])
            
            predicted_class = class_names[np.argmax(score)]
            confidence = 100 * np.max(score)
      
    


# Page configuration
st.set_page_config(
    page_title="AgriAI: Crop Disease Predictor",
    page_icon="🌿",
    layout="centered"
)

# App header
st.title("🌿 AgriAI: Crop Disease & Yield Protection")
st.markdown("Upload a photo of a crop leaf below to detect potential diseases instantly and protect your harvest.")

# Load the trained model (cached so it loads fast)
@st.cache_resource
def load_my_model():
    model = load_model('crop_disease_model.h5')
    return model

with st.spinner('Loading AI Model... Please wait!'):
    model = load_my_model()

# List of 38 PlantVillage class names matching your training order
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
    'OrangeHaunglongbing_(Citrus_greening)', 'PeachBacterial_spot', 'Peachhealthy',
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
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Crop Leaf', use_container_width=True)
    
    # Predict button
    if st.button('Analyze Leaf'):
        with st.spinner('Analyzing image for diseases...'):
            # Preprocess the image to match model expectations
            image = image.resize((160, 160))
            img_array = tf.keras.utils.img_to_array(image)
            img_array = tf.expand_dims(img_array, 0) # Create a batch
            
            # Make prediction
            predictions = model.predict(img_array)
            score = tf.nn.softmax(predictions[0])
            
            predicted_class = class_names[np.argmax(score)]
            confidence = 100 * np.max(score)
      
    
    	import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Page configuration
st.set_page_config(
    page_title="AgriAI: Crop Disease Predictor",
    page_icon="🌿",
    layout="centered"
)

# App header
st.title("🌿 AgriAI: Crop Disease & Yield Protection")
st.markdown("Upload a photo of a crop leaf below to detect potential diseases instantly and protect your harvest.")

# Load the trained model (cached so it loads fast)
@st.cache_resource
def load_my_model():
    model = load_model('crop_disease_model.h5')
    return model

with st.spinner('Loading AI Model... Please wait!'):
    model = load_my_model()

# List of 38 PlantVillage class names matching your training order
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
    'OrangeHaunglongbing_(Citrus_greening)', 'PeachBacterial_spot', 'Peachhealthy',
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
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Crop Leaf', use_container_width=True)
    
    # Predict button
    if st.button('Analyze Leaf'):
        with st.spinner('Analyzing image for diseases...'):
            # Preprocess the image to match model expectations
            image = image.resize((160, 160))
            img_array = tf.keras.utils.img_to_array(image)
            img_array = tf.expand_dims(img_array, 0) # Create a batch
            
            # Make prediction
            predictions = model.predict(img_array)
            score = tf.nn.softmax(predictions[0])
            
            predicted_class = class_names[np.argmax(score)]
            confidence = 100 * np.max(score)
      
    
            formatted_name = predicted_class.replace("_", " - ").replace("_", " ")
    st.success(f"Prediction: {formatted_name}")
    st.info(f"Confidence Score: {confidence:.2f}%")

    # Check if we have extra knowledge base info for this disease
    if predicted_class in DISEASE_INFO:
        info = DISEASE_INFO[predicted_class]

        st.warning(f"Estimated Severity Risk: {info['severity']}")

        with st.expander("📖 About the Disease", expanded=True):
            st.write(info["description"])

        with st.expander("🛠️ Immediate Management & Treatment", expanded=True):
            st.write(info["management"])

        with st.expander("🛡️ Long-Term Prevention", expanded=True):
            st.write(info["prevention"])
    else:
        st.info("Detailed management guidelines for this specific class will be available soon.")
