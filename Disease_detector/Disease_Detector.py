# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 13:03:46 2024

@author: azadk
"""



import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the models
diabetes_model = pickle.load(open('C:/Users/azadk/OneDrive/Desktop/projects/Disease_detector/diabetes2.sav', 'rb'))
parkinson_model = pickle.load(open('C:/Users/azadk/OneDrive/Desktop/projects/Disease_detector/parkinson_model.sav', 'rb'))
heart_model = pickle.load(open('C:/Users/azadk/OneDrive/Desktop/projects/Disease_detector/heart_disease_model.sav', 'rb'))


# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Disease Detector',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Predictor')
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col1:
        BloodPressure = st.text_input('Blood Pressure value')
    with col2:
        SkinThickness = st.text_input('Skin Thickness value')
    with col1:
        Insulin = st.text_input('Insulin Level')
    with col2:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    # Prediction
    diabetes_diagnosis = ''

    if st.button("Test Result"):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(i) for i in user_input]

        diabetes_prediction = diabetes_model.predict([user_input])

        if diabetes_prediction[0] == 1:
            diabetes_diagnosis = 'Diabetic'
        else:
            diabetes_diagnosis = 'Not Diabetic'

    st.success(diabetes_diagnosis)

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Predictor')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col2:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''

    if st.button('Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(i) for i in user_input]

        heart_prediction = heart_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'Heart Disease result positive'
        else:
            heart_diagnosis = 'No Heart Disease'

    st.success(heart_diagnosis)

# Parkinson Disease Prediction
if selected == 'Parkinson Prediction':
    st.title('Parkinson Disease Predictor')

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        fo = st.text_input('Fo(Hz)')
    with col2:
        fhi = st.text_input('Fhi(Hz)')
    with col3:
        flo = st.text_input('Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('Jitter(%)')
    with col1:
        Jitter_Abs = st.text_input('Jitter(Abs)')
    with col2:
        RAP = st.text_input('RAP')
    with col3:
        PPQ = st.text_input('PPQ')
    with col4:
        DDP = st.text_input('DDP')
    with col1:
        Shimmer = st.text_input('Shimmer')
    with col2:
        Shimmer_dB = st.text_input('Shimmer(dB)')
    with col3:
        APQ3 = st.text_input('APQ3')
    with col4:
        APQ5 = st.text_input('APQ5')
    with col1:
        APQ = st.text_input('APQ')
    with col2:
        DDA = st.text_input('DDA')
    with col3:
        NHR = st.text_input('NHR')
    with col4:
        HNR = st.text_input('HNR')
    with col1:
        RPDE = st.text_input('RPDE')
    with col2:
        DFA = st.text_input('DFA')
    with col3:
        spread1 = st.text_input('spread1')
    with col4:
        spread2 = st.text_input('spread2')
    with col2:
        D2 = st.text_input('D2')
    with col3:
        PPE = st.text_input('PPE')

    # Prediction
    parkinson_diagnosis = ''

    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(i) for i in user_input]

        parkinson_prediction = parkinson_model.predict([user_input])

        if parkinson_prediction[0] == 1:
            parkinson_diagnosis = "Parkinson's disease result positive"
        else:
            parkinson_diagnosis = "Parkinson's disease result negative"

    st.success(parkinson_diagnosis)


