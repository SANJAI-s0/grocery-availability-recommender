# backend/utils/helpers.py
# Utility helpers for the backend (DB + small helpers)

import pandas as pd
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"

def load_products_csv(filename="products.csv"):
    """
    Load product catalog CSV from data/raw/
    Returns pandas DataFrame.
    """
    path = RAW_DATA_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Products CSV not found at {path}")
    df = pd.read_csv(path)
    return df

def load_features_csv(filename="features.csv"):
    """
    Load processed features for ML training from data/processed/
    """
    path = PROCESSED_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Features CSV not found at {path}")
    df = pd.read_csv(path)
    return df

def save_products_to_db(session, df_products):
    """
    Given a SQLAlchemy session and products DataFrame, insert into products table
    if not already present. Returns number inserted.
    """
    from backend.database.db import Product

    inserted = 0
    for _, row in df_products.iterrows():
        exists = session.query(Product).filter_by(sku=str(row.get("sku"))).first()
        if not exists:
            p = Product(
                sku=str(row.get("sku")),
                name=str(row.get("name")),
                category=str(row.get("category")) if row.get("category") else None,
                price=float(row.get("price")) if row.get("price") else None
            )
            session.add(p)
            inserted += 1
    session.commit()
    return inserted
