# backend/models/__init__.py
# Helper functions to load ML models saved by training scripts.

import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")
AVAILABILITY_MODEL_PATH = os.path.join(MODEL_DIR, "availability_model.pkl")
REPLACEMENT_MODEL_PATH = os.path.join(MODEL_DIR, "replacement_model.pkl")

def load_availability_model():
    """
    Load and return the availability model.
    """
    if not os.path.exists(AVAILABILITY_MODEL_PATH):
        raise FileNotFoundError(f"Availability model not found at {AVAILABILITY_MODEL_PATH}")
    return joblib.load(AVAILABILITY_MODEL_PATH)

def load_replacement_model():
    """
    Load and return (vectorizer, similarity_matrix, product_names)
    """
    if not os.path.exists(REPLACEMENT_MODEL_PATH):
        raise FileNotFoundError(f"Replacement model not found at {REPLACEMENT_MODEL_PATH}")
    return joblib.load(REPLACEMENT_MODEL_PATH)
