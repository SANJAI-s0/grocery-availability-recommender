from flask import Flask, jsonify, request
from flask_cors import CORS
from pathlib import Path
import logging
import pandas as pd

from routes.availability import availability_bp
from routes.replacement import replacement_bp
from database.db import engine
from sqlalchemy import text
from models import load_availability_model, load_replacement_model

import subprocess
import logging

logging.info("🔄 Auto-training ML models...")
subprocess.run(["python", "backend/ml/train_availability.py"], check=False)
subprocess.run(["python", "backend/ml/train_replacement.py"], check=False)

# -------------------------------------------------
# App setup
# -------------------------------------------------
app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("backend")

# -------------------------------------------------
# IMPORTANT: DATA DIRECTORY (FIXED)
# -------------------------------------------------
# Docker volume mounts ./data → /app/data
DATA_DIR = Path("/app/data")

logger.info(f"DATA_DIR resolved to: {DATA_DIR}")

# -------------------------------------------------
# Blueprints
# -------------------------------------------------
app.register_blueprint(availability_bp, url_prefix="/api")
app.register_blueprint(replacement_bp, url_prefix="/api")

# -------------------------------------------------
# Root
# -------------------------------------------------
@app.route("/", methods=["GET"])
def home():
    return {
        "status": "ok",
        "service": "Grocery Availability Recommender",
        "backend": "http://localhost:5000",
        "frontend": "http://localhost:3000",
    }

# -------------------------------------------------
# Domains API
# -------------------------------------------------
@app.route("/api/domains", methods=["GET"])
def get_domains():
    if not DATA_DIR.exists():
        return jsonify({"error": "DATA_DIR missing", "path": str(DATA_DIR)}), 500

    domains = sorted(
        [
            d.name
            for d in DATA_DIR.iterdir()
            if d.is_dir() and (d / "processed" / "features.csv").exists()
        ]
    )

    return jsonify(domains)

# -------------------------------------------------
# Products API (DOMAIN BASED)
# -------------------------------------------------
@app.route("/api/products", methods=["GET"])
def get_products():
    domain = request.args.get("domain", "grocery")
    logger.info(f"Domain requested: {domain}")

    features_csv = DATA_DIR / domain / "processed" / "features.csv"
    logger.info(f"Looking for file: {features_csv}")

    if not features_csv.exists():
        return jsonify(
            {
                "error": f"Domain '{domain}' not found or features.csv missing",
                "expected_path": str(features_csv),
            }
        ), 404

    df = pd.read_csv(features_csv)

    required_cols = {"product_id", "name"}
    if not required_cols.issubset(df.columns):
        return jsonify(
            {
                "error": "features.csv missing required columns",
                "required": list(required_cols),
                "found": list(df.columns),
            }
        ), 500

    products = (
        df[["product_id", "name"]]
        .drop_duplicates()
        .rename(columns={"product_id": "id"})
        .to_dict(orient="records")
    )

    return jsonify(products)

# -------------------------------------------------
# Health
# -------------------------------------------------
@app.route("/health", methods=["GET"])
def health():
    db_ok = False
    models_ok = False

    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            db_ok = True
    except Exception as e:
        logger.error(f"DB error: {e}")

    try:
        load_availability_model()
        load_replacement_model()
        models_ok = True
    except Exception as e:
        logger.error(f"Model load error: {e}")

    return jsonify(
        {
            "status": "ok" if db_ok and models_ok else "degraded",
            "database": db_ok,
            "models_loaded": models_ok,
        }
    )

# -------------------------------------------------
# Main
# -------------------------------------------------
if __name__ == "__main__":
    logger.info("Starting backend service")
    logger.info("Backend → http://localhost:5000")
    logger.info("Frontend → http://localhost:3000")

    app.run(host="0.0.0.0", port=5000, debug=True)
