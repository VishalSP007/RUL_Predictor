import streamlit as st
import joblib
import json
import pandas as pd

# Load model and features
model = joblib.load("rul_model.pkl")
with open("features.json") as f:
    features = json.load(f)

st.set_page_config(page_title="Engine RUL Predictor", layout="centered")
st.title("🛩️ Aircraft Engine RUL Predictor")
st.write("Enter current cycle and sensor readings to predict Remaining Useful Life (RUL).")

# Input fields
inputs = {}
for feat in features:
    inputs[feat] = st.number_input(f"{feat}", value=0.0)

# Predict button
if st.button("Predict RUL"):
    X = pd.DataFrame([inputs])
    rul_pred = model.predict(X)[0]
    st.success(f"🔧 Predicted Remaining Useful Life (RUL): **{rul_pred:.2f} cycles**")