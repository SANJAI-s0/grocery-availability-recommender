import sys
import pandas as pd
from pathlib import Path
import hashlib

if len(sys.argv) != 2:
    print("Usage: python preprocess.py <domain>")
    sys.exit(1)

DOMAIN = sys.argv[1]

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "data" / DOMAIN / "raw"
PROCESSED_DIR = ROOT / "data" / DOMAIN / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

RAW_CSV = RAW_DIR / "products.csv"
OUT_CSV = PROCESSED_DIR / "features.csv"

if not RAW_CSV.exists():
    raise FileNotFoundError(f"{RAW_CSV} not found")

df = pd.read_csv(RAW_CSV)

required_cols = {"product_id", "name"}
missing = required_cols - set(df.columns)
if missing:
    raise ValueError(f"products.csv missing columns: {missing}")

def stable_hash(value: str) -> int:
    return int(hashlib.md5(value.encode()).hexdigest(), 16)

df["sales"] = df["name"].apply(lambda x: (stable_hash(x) % 50) + 1)
df["day"] = df["product_id"].apply(lambda x: (x % 7) + 1)

df["available"] = df.apply(
    lambda r: 0 if (r["sales"] > 35 and r["day"] in [5, 6, 7]) else 1,
    axis=1
)

features = df[
    ["product_id", "name", "sales", "day", "available"]
]

features.to_csv(OUT_CSV, index=False)

print("✅ Preprocessing completed")
print(f"🏷️ Domain: {DOMAIN}")
print(f"📦 Products processed: {len(features)}")
print(f"💾 Output written to: {OUT_CSV}")
