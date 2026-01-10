from flask import Blueprint, request, jsonify
from models import load_replacement_model

replacement_bp = Blueprint("replacement", __name__)

@replacement_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json() or {}
    domain = data.get("domain", "grocery")
    name = data.get("name")

    model = load_replacement_model(domain)
    products = model["products"]
    similarity = model["similarity"]

    if name not in products:
        return jsonify({"replacements": []})

    idx = products.index(name)
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    return jsonify({
        "replacements": [
            products[i] for i, s in scores[1:6] if s > 0.1
        ]
    })
