from flask import Flask, jsonify
from flask_cors import CORS
import os

# Blueprints
from routes.availability import availability_bp
from routes.replacement import replacement_bp

# Optional: DB & model checks for health endpoint
from sqlalchemy import text
from database.db import engine
from models import load_availability_model, load_replacement_model

app = Flask(__name__)
CORS(app)

# ------------------------------------------------------------------
# Register API blueprints
# ------------------------------------------------------------------
app.register_blueprint(availability_bp, url_prefix="/api")
app.register_blueprint(replacement_bp, url_prefix="/api")

# ------------------------------------------------------------------
# Root endpoint
# ------------------------------------------------------------------
@app.route("/", methods=["GET"])
def home():
    return {
        "message": "Grocery Availability Recommender API running",
        "status": "ok"
    }

# ------------------------------------------------------------------
# Health check endpoint (for Docker / production)
# ------------------------------------------------------------------
@app.route("/health", methods=["GET"])
def health():
    db_ok = False
    models_ok = False

    # Check database connectivity
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            db_ok = True
    except Exception:
        db_ok = False

    # Check ML models load correctly
    try:
        load_availability_model()
        load_replacement_model()
        models_ok = True
    except Exception:
        models_ok = False

    overall_status = "ok" if db_ok and models_ok else "degraded"

    return jsonify({
        "status": overall_status,
        "database": "ok" if db_ok else "error",
        "models_loaded": models_ok,
        "environment": os.getenv("FLASK_ENV", "production")
    })

# ------------------------------------------------------------------
# App entry point
# ------------------------------------------------------------------
if __name__ == "__main__":
    # NOTE:
    # - Flask dev server is OK for local testing
    # - In Docker / production, use Gunicorn instead
    app.run(host="0.0.0.0", port=5000, debug=True)
