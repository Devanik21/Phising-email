import streamlit as st
import rarfile
import joblib
import os
import urllib.request

# URL of the .rar file in your GitHub repo
url = "Phishing_email_RF.rar"

# Download the .rar file
rar_filename = "Phishing_email_RF.rar"
if not os.path.exists(rar_filename):
    st.write("Downloading the model...")
    urllib.request.urlretrieve(url, rar_filename)

# Extract the .rar file
extracted_folder = "extracted_model"
if not os.path.exists(extracted_folder):
    os.makedirs(extracted_folder)

    st.write("Extracting the model...")
    with rarfile.RarFile(rar_filename) as rf:
        rf.extractall(extracted_folder)

# Load the model (assuming the extracted file is a .pkl file)
model_path = os.path.join(extracted_folder, "Phishing_email_RF.pkl")
model = joblib.load(model_path)

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
