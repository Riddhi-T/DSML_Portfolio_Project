from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

# Create Flask app
app = Flask(__name__)

# Load the trained model
MODEL_PATH = os.path.join("..", "model", "XGBoost_Tuned_model.pkl")
model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET"])
def home():
    return "Insurance Cost Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    """
    Expects JSON input for features.
    """

    data = request.get_json()

    # Extract features in correct order
    features = np.array([
        data["age"],
        data["diabetes"],
        data["bp"],
        data["transplant"],
        data["chronic_disease"],
        data["allergies"],
        data["hist_cancer"],
        data["bmi"],
        data["surgeries"]
    ]).reshape(1, -1)

    # Make prediction
    prediction = model.predict(features)[0]

    # Return result as JSON
    return jsonify({
        "predicted_cost": float(prediction)
    })

if __name__ == "__main__":
    app.run(debug=True)
