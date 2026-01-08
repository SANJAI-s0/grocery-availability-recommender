# backend/utils/preprocess.py
# Create a simple features.csv (sales, day, available) from products.csv
# This is intentionally simple and deterministic to be reproducible for demo.

import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def build_features(products_csv="products.csv", out_csv="features.csv"):
    products_path = RAW_DIR / products_csv
    if not products_path.exists():
        raise FileNotFoundError(f"{products_path} not found. Place products CSV at data/raw/")

    df = pd.read_csv(products_path)

    # create deterministic synthetic sales/day/availability columns:
    # Sales: based on hash of name mod 40
    # Day: 1..7 (weekday)
    # Available: set to 0 if sales > threshold to simulate stockout
    sales = df['name'].apply(lambda s: (abs(hash(s)) % 40) + 1)
    day = df['name'].apply(lambda s: (abs(hash(s)) % 7) + 1)
    threshold = 30  # higher sales -> more chance of stockout for demo
    available = sales.apply(lambda v: 0 if v > threshold else 1)

    features = pd.DataFrame({
        'product_id': df.get('product_id', pd.Series(range(1, len(df)+1))),
        'name': df['name'],
        'sales': sales,
        'day': day,
        'available': available
    })

    out_path = PROCESSED_DIR / out_csv
    features.to_csv(out_path, index=False)
    print(f"Wrote features to {out_path}")
    return features

if __name__ == "__main__":
    build_features()
