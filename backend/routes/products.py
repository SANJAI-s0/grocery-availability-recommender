from flask import Blueprint, request, jsonify
from pathlib import Path
import pandas as pd

products_bp = Blueprint("products", __name__)

# root/data/<domain>/processed/features.csv
DATA_ROOT = Path(__file__).resolve().parents[2] / "data"

@products_bp.route("/products", methods=["GET"])
def get_products():
    domain = request.args.get("domain")

    if not domain:
        return jsonify({"error": "domain query parameter is required"}), 400

    features_path = DATA_ROOT / domain / "processed" / "features.csv"

    if not features_path.exists():
        return jsonify({"error": f"No data found for domain '{domain}'"}), 404

    df = pd.read_csv(features_path)

    products = (
        df[["product_id", "name"]]
        .drop_duplicates()
        .rename(columns={"product_id": "id"})
        .to_dict(orient="records")
    )

    return jsonify(products)
