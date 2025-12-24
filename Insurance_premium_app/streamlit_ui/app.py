import streamlit as st
import numpy as np
import requests
st.markdown("""
<style>
/* Page background */
[data-testid="stAppViewContainer"] {
    background-color: #88BDBC;  /* Soft Teal */
}

/* Card / main container */
section.main {
    background-color: #FFFFFF;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

/* Number input and text input - remove borders */
div.stNumberInput,
div.stTextInput > div > input {
    border: none;
    padding: 5px 10px;
    border-radius: 5px;
}

/* Selectbox - leave default styling (no borders) */
div.stSelectbox > div {
    border: none;
    padding: 5px 10px;
    border-radius: 5px;
}

/* Optional: maintain hover effect for number/text input */
div.stNumberInput:hover,
div.stTextInput > div > input:hover {
    outline: 1px solid #4CAF50;
}

/* Ensure selectbox text is fully visible */
div.stSelectbox div.css-1wa3eu0 {
    overflow: visible !important;
}

/* Shift input labels slightly to the right */
label {
    font-family: 'Arial', sans-serif;
    font-size: 25px;
    font-weight: 500;
    color: #333333;
    margin-left: 10px;  /* adjust this value to shift */
    display: block;     /* ensures label stays above the input */
}
</style>
""", unsafe_allow_html=True)



st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("Insurance Cost Predictor")
st.write("Estimate your insurance premium in real time")
#st.write("Estimate your insurance premium")


with st.form("insurance_form"):
    # Row 1
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", 1, 100, 30)
    with col2:
        bmi = st.number_input("BMI", 0.0, 50.0, 24.0)
    with col3:
        allergies = st.selectbox("Any known allergies?", ['No', 'Yes'])
    st.write("")

    # Row 2
    col1, col2 = st.columns(2)
    with col1:
        bp = st.selectbox("Do you have any blood pressure problems?", ['No','Yes'])
    with col2:
        diabetes = st.selectbox("Do you have Diabetes?", ['No','Yes'])
    st.write("")
    
    # Row 3
    col1, col2 = st.columns(2)
    with col1:
        chronic_disease = st.selectbox("Any chronic illnesses?", ['No','Yes'])
    with col2:
        hist_cancer = st.selectbox("Family history of cancer?", ['No','Yes'])
    st.write("")
    
    # Row 4
    col1, col2 = st.columns(2)
    with col1:
        surgeries = st.selectbox("How many major surgeries have you had?", [0, 1,'2 or more'])
    with col2:
        transplant = st.selectbox("Any transplant surgeries?", ['No','Yes'])
    st.write("")

    submit = st.form_submit_button("Predict") 


if submit:

    allergies_val = 1 if allergies == "Yes" else 0
    bp_val = 1 if bp == "Yes" else 0
    diabetes_val = 1 if diabetes == "Yes" else 0
    chronic_disease_val = 1 if chronic_disease == "Yes" else 0
    hist_cancer_val = 1 if hist_cancer == "Yes" else 0
    transplant_val = 1 if transplant == "Yes" else 0
    surgeries_val = 2 if surgeries =='2 or more' else surgeries
    
    with st.spinner("Calculating your insurance premium..."):
        response = requests.post(
        "http://127.0.0.1:5000/predict",
        json={
            "age": age,
            "diabetes" : diabetes_val,
            "bp" : bp_val,
            "transplant" : transplant_val,
            "chronic_disease" : chronic_disease_val,
            "allergies" : allergies_val,
            "hist_cancer" : hist_cancer_val,
            "bmi": bmi,
            "surgeries" : surgeries_val 
        }
    )
        result = response.json()
    #st.success(f"Your estimated premium cost is INR: {result['predicted_cost']:.2f}")
    st.metric(label="Estimated Annual Premium", value=f"{result['predicted_cost']:.2f} INR")
    st.caption("This is an estimate based on your input health data.")

    



