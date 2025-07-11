import streamlit as st
import pandas as pd
import joblib

model = joblib.load("C:\\Users\\Lenovo\\OneDrive\\Desktop\\Heart disease\\KNN_heart.pkl")
scaler = joblib.load("C:\\Users\\Lenovo\\OneDrive\\Desktop\\Heart disease\\scaler.pkl")
expected_columns = joblib.load("C:\\Users\\Lenovo\\OneDrive\\Desktop\\Heart disease\\columns.pkl")

st.title("Heart Disease Prediction App")
st.markdown("Provide the required inputs to predict the likelihood of heart disease.")

age = st.slider("Age", 0, 120, 30)
sex = st.selectbox("Sex", ['M', 'F'])
chestpain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
chol = st.number_input("Cholesterol(mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting Electrocardiographic Results", ["Normal","ST","LVH"])
max_hr = st.slider("Maximum Heart Rate Achieved", 60, 200, 150)
exercise_ecg = st.selectbox("Exercise Induced Angina", ["Y", "N"])
oldpeak = st.slider("Depression Induced by Exercise Relative to Rest", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of the Peak Exercise ST Segment", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0-3) Colored by Fluoroscopy", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

if st.button("Predict"):
    raw_data = {
        'age': age,
        'sex': sex,
        'chestpain': chestpain,
        'resting_bp': resting_bp,
        'chol': chol,
        'fasting_bs': fasting_bs,
        'restecg': restecg,
        'max_hr': max_hr,
        'exercise_ecg': exercise_ecg,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }

    input_df = pd.DataFrame([raw_data])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]
    
    if prediction == 1:
        st.error("The model predicts that you are likely to have heart disease.")
    else:
        st.success("The model predicts that you are unlikely to have heart disease.")
