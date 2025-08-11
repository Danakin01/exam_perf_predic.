import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

model = joblib.load('model.pkl')

st.title("🎓 Student Performance Prediction")
st.markdown("This app predicts the **exam score** based on various student characteristics.")

st.markdown("---")

with st.container():
    st.header("📋 Input Student Details")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        Hours_Studied = st.number_input("Hours Studied (per week)", min_value=0, max_value=50, value=10)
        Attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=75)
        Sleep_Hours = st.number_input("Sleep Hours (per night)", min_value=0, max_value=12, value=7)
        Previous_Scores = st.number_input("Previous Scores", min_value=0, max_value=100, value=70)
        Tutoring_Sessions = st.number_input("Tutoring Sessions (per week)", min_value=0, max_value=10, value=2)
        Physical_Activity = st.number_input("Physical Activity (hours per week)", min_value=0, max_value=20, value=5)

    with col2:
        Parental_Involvement = st.selectbox("Parental Involvement", ["Low", "Medium", "High"])
        Access_to_Resources = st.selectbox("Access to Resources", ["Low", "Medium", "High"])
        Extracurricular_Activities = st.selectbox("Extracurricular Activities", ["No", "Yes"])
        Motivation_Level = st.selectbox("Motivation Level", ["Low", "Medium", "High"])
        Internet_Access = st.selectbox("Internet Access", ["No", "Yes"])
        Family_Income = st.selectbox("Family Income", ["Low", "Medium", "High"])

    with col3:
        Teacher_Quality = st.selectbox("Teacher Quality", ["Low", "Medium", "High"])
        School_Type = st.selectbox("School Type", ["Public", "Private"])
        Peer_Influence = st.selectbox("Peer Influence", ["Negative", "Neutral", "Positive"])
        Learning_Disabilities = st.selectbox("Learning Disabilities", ["No", "Yes"])
        Parental_Education_Level = st.selectbox("Parental Education Level", ["High School", "College", "Postgraduate"])
        Distance_from_Home = st.selectbox("Distance from Home", ["Near", "Moderate", "Far"])
        Gender = st.selectbox("Gender", ["Female", "Male"])

# --- Encode Categorical Variables (manually or using one-hot logic as in training)
def preprocess_input():
    data = pd.DataFrame({
        "Hours_Studied": [Hours_Studied],
        "Attendance": [Attendance],
        "Sleep_Hours": [Sleep_Hours],
        "Previous_Scores": [Previous_Scores],
        "Tutoring_Sessions": [Tutoring_Sessions],
        "Physical_Activity": [Physical_Activity],
        "Parental_Involvement": [Parental_Involvement],
        "Access_to_Resources": [Access_to_Resources],
        "Extracurricular_Activities": [Extracurricular_Activities],
        "Motivation_Level": [Motivation_Level],
        "Internet_Access": [Internet_Access],
        "Family_Income": [Family_Income],
        "Teacher_Quality": [Teacher_Quality],
        "School_Type": [School_Type],
        "Peer_Influence": [Peer_Influence],
        "Learning_Disabilities": [Learning_Disabilities],
        "Parental_Education_Level": [Parental_Education_Level],
        "Distance_from_Home": [Distance_from_Home],
        "Gender": [Gender]
    })

    # Apply same encoding as during training
    # This should ideally be a saved transformer: joblib.load("preprocessor.pkl")
    data_encoded = pd.get_dummies(data)

    # Align with model features
    expected_features = model.feature_names_in_  # If available
    data_encoded = data_encoded.reindex(columns=expected_features, fill_value=0)
    
    return data_encoded

# --- Predict
if st.button("🔍 Predict Exam Score"):
    with st.spinner("Predicting..."):
        try:
            processed_input = preprocess_input()
            prediction = model.predict(processed_input)
            st.success(f"🎯 Predicted Exam Score: **{prediction[0]:.2f}**")
        except Exception as e:
            st.error(f"Error in prediction: {e}")
