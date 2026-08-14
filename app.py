import streamlit as st
import tensorflow as tf
import numpy as np
import json
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Crop Leaf Disease Detector",
    page_icon="🌿",
    layout="centered"
)

# Load Model and Class Names (cached for performance)
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('plant_disease_model.keras')
    return model

@st.cache_data
def load_class_names():
    with open('class_names.json', 'r') as f:
        class_names = json.load(f)
    return class_names

model = load_model()
class_names = load_class_names()

# Knowledge base for prevention, medication, and cure info
disease_info = {
    "default": {
        "description": "Plant disease detected from leaf image analysis.",
        "prevention": "Ensure proper spacing between crops, maintain clean field sanitation, and avoid overhead watering.",
        "medication": "Apply recommended organic or chemical fungicides/bactericides depending on severity."
    }
}

# UI Layout
st.title("🌿 Crop Leaf Disease Detection App")
st.write("Upload a clear photo of a crop leaf to identify diseases and get instant treatment recommendations for your farm.")

uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Leaf Image', use_container_width=True)
    
    if st.button('Analyze Leaf'):
        with st.spinner('Analyzing image for diseases...'):
            # Preprocess image
            image = image.resize((224, 224))
            img_array = np.array(image)
            
            # Handle alpha channel if PNG has transparency
            if img_array.shape[-1] == 4:
                img_array = img_array[..., :3]
                
            img_array = np.expand_dims(img_array, axis=0)
            
            # Predict
            predictions = model.predict(img_array)
            predicted_class_index = np.argmax(predictions[0])
            confidence = float(np.max(predictions[0])) * 100
            
            predicted_class_name = class_names[predicted_class_index]
            
        # Display Results
        st.success(f"Diagnosis: {predicted_class_name.replace('___', ' - ').replace('_', ' ')}")
        st.info(f"Confidence: {confidence:.2f}%")
        
        # Recommendations
        st.markdown("### 💊 Treatment & Management Recommendations")
        info = disease_info.get(predicted_class_name, disease_info["default"])
        
        st.markdown(f"Prevention:\n{info['prevention']}")
        st.markdown(f"Medication & Cure:\n{info['medication']}")
