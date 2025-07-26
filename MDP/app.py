import streamlit as st
import numpy as np
import pickle

# Load the model
with open('diabetes_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🩺 Diabetes Prediction App")

# Input fields
age = st.number_input("Age")
bmi = st.number_input("BMI")
bp = st.number_input("Blood Pressure")
s1 = st.number_input("S1 (TC)")
s2 = st.number_input("S2 (LDL)")
s3 = st.number_input("S3 (HDL)")
s4 = st.number_input("S4 (TCH)")
s5 = st.number_input("S5 (LTG)")
s6 = st.number_input("S6 (GLU)")

if st.button("Predict"):
    input_data = np.array([[age, bmi, bp, s1, s2, s3, s4, s5, s6]])
    result = model.predict(input_data)
    if result[0] == 1:
        st.error("⚠️ You may be at risk of Diabetes.")
    else:
        st.success("✅ You are likely not at risk of Diabetes.")
