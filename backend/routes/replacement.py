from flask import Blueprint, request, jsonify
import joblib

replacement_bp = Blueprint("replacement", __name__)
vectorizer, similarity_matrix, product_names = joblib.load(
    "models/replacement_model.pkl"
)

@replacement_bp.route("/recommend", methods=["POST"])
def recommend():
    item = request.json["item"]
    idx = product_names.index(item)
    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:4]

    recommendations = [product_names[i] for i, _ in scores]
    return jsonify({"replacements": recommendations})
