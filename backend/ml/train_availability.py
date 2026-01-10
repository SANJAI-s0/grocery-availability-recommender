import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
MODEL_DIR = ROOT / "backend" / "models" / "availability"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

trained = False

for domain_dir in DATA_DIR.iterdir():
    features_path = domain_dir / "processed" / "features.csv"
    if not features_path.exists():
        continue

    df = pd.read_csv(features_path)

    X = df[["sales", "day"]]
    y = df["available"]

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    out_path = MODEL_DIR / f"{domain_dir.name}.pkl"
    joblib.dump(model, out_path)

    print(f"✅ Trained availability model for domain: {domain_dir.name}")
    trained = True

if not trained:
    raise RuntimeError("No domains found with processed data")
