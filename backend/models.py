import joblib
from pathlib import Path

BASE = Path(__file__).resolve().parent / "models"

def load_availability_model(domain):
    path = BASE / "availability" / f"{domain}.pkl"
    if not path.exists():
        raise FileNotFoundError(f"Availability model missing for {domain}")
    return joblib.load(path)

def load_replacement_model(domain):
    path = BASE / "replacement" / f"{domain}.pkl"
    if not path.exists():
        raise FileNotFoundError(f"Replacement model missing for {domain}")
    return joblib.load(path)
