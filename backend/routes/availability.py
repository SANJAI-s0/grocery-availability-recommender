from flask import Blueprint, request, jsonify
import joblib
import numpy as np

availability_bp = Blueprint("availability", __name__)
model = joblib.load("models/availability_model.pkl")

@availability_bp.route("/predict-availability", methods=["POST"])
def predict_availability():
    data = request.json
    features = np.array([[data["sales"], data["day"]]])
    prediction = model.predict(features)[0]

    return jsonify({
        "available": bool(prediction)
    })
