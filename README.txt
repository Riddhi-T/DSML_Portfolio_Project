Insurance Premium Cost Prediction

This repository contains scripts and files for a short project on Insurance Premium Cost Prediction. The project includes data analysis, machine learning modeling, and a web-based application for premium estimation using Streamlit and Flask API.

Folder Structure
1. 1_Tableau_Visualization

Contains the original Tableau workbook for dashboard creation.

Includes input CSV files required for the visualization.

README file inside this folder contains insights, recommendations, and a link to the Tableau Public Dashboard.

2. 2_EDA_and_Hypothesis_Testing

Python scripts for exploratory data analysis (EDA) and hypothesis testing.

Input CSV file: insurance_1.csv (located in ./1_Tableau_Visualization).

Provides statistical insights into the data and relationships between variables.

3. 3_ML_modeling

Scripts for model training, evaluation, and post-prediction analysis.

Input CSV file: ml_input.csv.

The models folder contains saved machine learning models in .pkl format.

Focus is on the XGBoost model, which performs best for this dataset.

4. Insurance_premium_app

Contains scripts to integrate the final XGBoost model into a web-based Premium Cost estimation tool.

Includes both Flask API backend and Streamlit UI frontend.

The model folder contains the saved XGBoost model used in the app.

How to run the app locally:

Download or clone the repository.

Start Flask API backend:

Navigate to the flask_api folder in the command line.

Run:

python app.py


This will start the Flask server to handle API requests.

Start Streamlit frontend:

Navigate to the streamlit_ui folder in the command line.

Run:

streamlit run app.py


This will open a web page hosting the premium prediction app.

Use the app:

Fill out the required details in the form.

Press Predict to get an estimated insurance premium.

Additional Notes

The Streamlit UI communicates with the Flask API for real-time predictions.

Only the final XGBoost model is deployed in the app.

All scripts are self-contained and can be run locally without any cloud service.
