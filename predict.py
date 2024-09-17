# predict.py

import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the pre-trained model (make sure to change the path to where your model is stored)
model = joblib.load('Phishing_email_RF')

# Title of the app
st.title("Phishing Email Detection")

# Add a brief description
st.write("""
This app predicts whether an email is phishing or legitimate based on user input features.
""")

# Input fields for user
st.header("Input Email Features")

# Example input features (modify according to your dataset)
url_features = st.text_input("URL Features (separated by commas)")
html_features = st.text_input("HTML Features (separated by commas)")
email_subject_length = st.number_input("Email Subject Length", min_value=0)
email_body_length = st.number_input("Email Body Length", min_value=0)

# Convert input into a feature vector (example)
if st.button("Predict"):
    # Assuming the features are URL, HTML, subject length, and body length
    try:
        # Convert the text inputs into a list of floats
        url_features = [float(i) for i in url_features.split(",")]
        html_features = [float(i) for i in html_features.split(",")]
        features = np.array(url_features + html_features + [email_subject_length, email_body_length]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)
        
        # Show prediction result
        if prediction[0] == 1:
            st.error("The email is predicted as Phishing!")
        else:
            st.success("The email is predicted as Legitimate!")
    except ValueError:
        st.error("Please enter valid inputs for the features.")

# Footer
st.write("Developed by Nik")
