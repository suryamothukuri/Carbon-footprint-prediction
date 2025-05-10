import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("catboost_emission_model.pkl")

st.title("🌿 Carbon Emission Estimator")
st.markdown("Usable AI - Project Demo")
st.markdown("Surya Teja mothukuri - smothuk@iu.edu")

st.markdown("Fill in your lifestyle details to estimate your monthly carbon emissions:")


col1, col2, col3 = st.columns(3)

with col1:
    body_type = st.selectbox("Body Type", ["Slim", "Average", "Overweight"])
    sex = st.selectbox("Sex", ["Male", "Female"])
    diet = st.selectbox("Diet", ["Omnivore", "Vegetarian", "Vegan"])
    shower_freq = st.slider("Shower/week", 0, 21, 7)
    heating_source = st.selectbox("Heating Energy", ["Gas", "Electric", "Wood", "None"])
    transport = st.selectbox("Transport", ["Car", "Public Transport", "Bike", "Walk"])

with col2:
    social_activity = st.slider("Social Activity/week", 0, 14, 3)
    grocery_bill = st.number_input("Monthly Grocery ($)", 100, 2000, 400)
    flight_freq = st.slider("Flight Trips/year", 0, 20, 2)
    vehicle_distance = st.slider("Monthly Vehicle Km", 0, 5000, 500)
    waste_bag_size = st.selectbox("Waste Bag Size", ["Small", "Medium", "Large"])
    waste_bag_count = st.slider("Waste Bags/week", 0, 10, 2)

with col3:
    tv_pc_hours = st.slider("Daily TV/PC Hours", 0, 24, 4)
    clothes_count = st.slider("Clothes/month", 0, 20, 2)
    internet_hours = st.slider("Internet Hours/day", 0, 24, 5)
    energy_eff = st.selectbox("Energy Efficient?", ["Yes", "No"])
    recycling = st.selectbox("Recycling Level", ["Never", "Sometimes", "Always"])
    cooking_with = st.selectbox("Cooking Fuel", ["Gas", "Electric", "Wood"])

input_data = pd.DataFrame([[
    {"Slim": 0, "Average": 1, "Overweight": 2}[body_type],
    0 if sex == "Male" else 1,
    {"Omnivore": 0, "Vegetarian": 1, "Vegan": 2}[diet],
    shower_freq,
    {"Gas": 0, "Electric": 1, "Wood": 2, "None": 3}[heating_source],
    {"Car": 0, "Public Transport": 1, "Bike": 2, "Walk": 3}[transport],
    social_activity,
    grocery_bill,
    flight_freq,
    vehicle_distance,
    {"Small": 0, "Medium": 1, "Large": 2}[waste_bag_size],
    waste_bag_count,
    tv_pc_hours,
    clothes_count,
    internet_hours,
    1 if energy_eff == "Yes" else 0,
    {"Never": 0, "Sometimes": 1, "Always": 2}[recycling],
    {"Gas": 0, "Electric": 1, "Wood": 2}[cooking_with]
]], columns=[
    'Body Type', 'Sex', 'Diet', 'How Often Shower', 'Heating Energy Source',
    'Transport', 'Social Activity', 'Monthly Grocery Bill',
    'Frequency of Traveling by Air', 'Vehicle Monthly Distance Km',
    'Waste Bag Size', 'Waste Bag Weekly Count', 'How Long TV PC Daily Hour',
    'How Many New Clothes Monthly', 'How Long Internet Daily Hour',
    'Energy efficiency', 'Recycling', 'Cooking_With'
])


if st.button("Estimate Emission"):
    scaler = joblib.load("scaler.pkl")
    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)[0]
    st.success(f"🌍 Estimated Monthly Carbon Emission: {prediction:.2f} kg CO₂")