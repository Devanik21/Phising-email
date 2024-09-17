import streamlit as st
import gdown  # You'll need to install this package
import joblib
import os

# Define the URL of your Google Drive file
url = 'https://drive.google.com/file/d/12Nbn9K2h3TqRgcUVOw_b-pLNT5yadapG/view?usp=drive_link'

# Download the file from Google Drive (only if it does not exist locally)
if not os.path.exists('Phishing_email_RF.pkl'):
    gdown.download(url, 'Phishing_email_RF.pkl', quiet=False)

# Load the model
model = joblib.load('Phishing_email_RF.pkl')

# Your prediction logic goes here


# Now you can use the model for predictions
st.title("Phishing Email Detection")
email_features = st.text_input("Enter email features (comma-separated)")

if st.button("Predict"):
    # Convert input into a feature vector (example)
    features = [float(x) for x in email_features.split(",")]
    prediction = model.predict([features])
    
    if prediction[0] == 1:
        st.error("This email is predicted as Phishing!")
    else:
        st.success("This email is predicted as Legitimate!")
