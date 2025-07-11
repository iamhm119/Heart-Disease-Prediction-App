# 🫀 Heart Disease Prediction App

This project is a Streamlit web application that predicts the likelihood of heart disease using a trained K-Nearest Neighbors (KNN) model. It takes user input for various medical parameters and returns a prediction indicating the risk of heart disease.

## 🔧 Files Included
- `app.py`: Streamlit app for frontend and prediction logic
- `KNN_heart.pkl`: Trained KNN model file
- `scaler.pkl`: Scaler used during training for feature normalization
- `columns.pkl`: List of expected input features for the model
- `Heart.ipynb`: Jupyter notebook used for data preprocessing, model training, and evaluation

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
2. pip install streamlit pandas scikit-learn joblib
3. streamlit run app.py

## 🧠 Model
The model is trained using the K-Nearest Neighbors (KNN) algorithm, and includes preprocessing steps like scaling and encoding. All components are saved as .pkl files for reuse in the app.

## 📊 Input Features
Age
Sex
Chest Pain Type
Resting Blood Pressure
Cholesterol
Fasting Blood Sugar
Resting ECG
Max Heart Rate
Exercise Induced Angina
Oldpeak
Slope
Number of Vessels
Thalassemia

## 📌 Note
Ensure the .pkl files (KNN_heart.pkl, scaler.pkl, columns.pkl) are in the same directory as app.py or update the paths accordingly in the code.
