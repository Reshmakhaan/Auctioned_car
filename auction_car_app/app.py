import streamlit as st
import pandas as pd
import pickle

# Load model
import os
model = pickle.load(open(os.path.join(os.path.dirname(__file__), 'model.pkl'), 'rb'))


st.title("🚗 Auctioned Car Risk Predictor")
st.markdown("Predict if the car is a **bad buy** at an auction.")

vehicle_age = st.slider("Vehicle Age (Years)", 0, 10, 3)
odometer = st.number_input("Odometer Reading", 1000, 200000, 60000)
auction = st.selectbox("Auction House", ["MANHEIM", "ADESA", "OTHER"])

if st.button("Predict"):
    auction_map = {"MANHEIM": 0, "ADESA": 1, "OTHER": 2}
    input_data = pd.DataFrame([{
        "VehicleAge": vehicle_age,
        "VehOdo": odometer,
        "Auction": auction_map.get(auction, 2),
    }])
    
    prediction = model.predict(input_data)[0]
    result = "❌ Bad Buy" if prediction == 1 else "✅ Good Buy"
    st.subheader(f"Prediction: {result}")
