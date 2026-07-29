predicted_class = st.session_state.predicted_class
        confidence = st.session_state.confidence

        formatted_name = predicted_class.replace('_', ' ').strip('-')
        st.success(f"Prediction: {formatted_name}")
        st.info(f"Confidence Score: {confidence:.2f}%")

        if predicted_class in DISEASE_INFO:
            info = DISEASE_INFO[predicted_class]
            severity_risk = info['severity']
            desc = info['description']
            mgmt = info['management']
            prev = info['prevention']
        else:
            severity_risk = "Moderate to High"
            desc = f"Pathogen identified in category: {formatted_name}. This impacts normal cellular function and foliage health."
            mgmt = "Isolate affected crops, prune severely damaged foliage, and apply an appropriate targeted treatment."
            prev = "Ensure correct plant spacing, avoid overhead watering, and maintain clean field sanitation."

        st.warning(f"Estimated Severity Risk: {severity_risk}")

        st.markdown("### 📋 Disease Management & Treatment Protocols")
        
        with st.expander("📖 About the Disease / Cause", expanded=True):
            st.write(desc)

        with st.expander("🛠️ Immediate Management & Treatment", expanded=True):
            st.write(mgmt)

        with st.expander("🛡️ Long-Term Prevention", expanded=True):
            st.write(prev)
