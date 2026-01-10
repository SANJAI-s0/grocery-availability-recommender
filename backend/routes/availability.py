from flask import Blueprint, request, jsonify
from models import load_availability_model

availability_bp = Blueprint("availability", __name__)

@availability_bp.route("/predict-availability", methods=["POST"])
def predict():
    data = request.get_json() or {}
    domain = data.get("domain", "grocery")

    model = load_availability_model(domain)

    sales = data["sales"]
    day = data["day"]

    prob = model.predict_proba([[sales, day]])[0]
    confidence = float(prob[1])
    available = confidence >= 0.5

    return jsonify({
        "available": available,
        "confidence": round(confidence, 3)
    })
