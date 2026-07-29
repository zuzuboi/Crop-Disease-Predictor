# disease_info.py - Division 2: Treatment, Cure, and Prevention Database

DATABASE = {
    "TomatoSeptoria_leaf_spot": {
        "cause": "Caused by the fungus Septoria lycopersici, which spreads via water splashes from infected debris onto lower leaves.",
        "cure": "Remove and destroy infected lower leaves immediately. Apply a certified copper- or chlorothalonil-based fungicide.",
        "prevention": "Use drip irrigation to keep foliage dry, stake plants properly, and practice a 3-year crop rotation."
    },
    "TomatoEarly_blight": {
        "cause": "Fungal pathogen Alternaria solani, which thrives in warm, wet conditions and attacks older leaves first.",
        "cure": "Prune heavily infected branches to improve air circulation and treat with appropriate organic or chemical fungicides.",
        "prevention": "Apply heavy mulch beneath plants to prevent soil splashing and ensure proper plant spacing."
    },
    "Corn_(maize)Common_rust_": {
        "cause": "Puccinia sorghi fungus, which produces pustules on leaf surfaces and is spread by wind-blown spores.",
        "cure": "Apply foliar fungicides if disease pressure is high and crops are in critical growth stages.",
        "prevention": "Plant genetically resistant corn hybrids and clear out crop residue completely after harvest."
    }
}

def get_disease_details(predicted_class, formatted_name):
    if predicted_class in DATABASE:
        info = DATABASE[predicted_class]
        return info["cause"], info["cure"], info["prevention"]
    else:
        cause = f"Pathogen identified under classification: {formatted_name}. This impacts normal cellular function and foliage health."
        cure = "Isolate affected crops, prune severely damaged foliage, and apply an appropriate targeted treatment."
        prevention = "Ensure correct plant spacing, avoid overhead watering, and maintain clean field sanitation."
        return cause, cure, prevention