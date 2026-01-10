import joblib
import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
MODEL_DIR = ROOT / "backend" / "models" / "replacement"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

for domain_dir in DATA_DIR.iterdir():
    features_path = domain_dir / "processed" / "features.csv"
    if not features_path.exists():
        continue

    df = pd.read_csv(features_path)
    names = df["name"].astype(str).tolist()

    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
    vectors = vectorizer.fit_transform(names)
    similarity = cosine_similarity(vectors)

    joblib.dump(
        {
            "products": names,
            "similarity": similarity
        },
        MODEL_DIR / f"{domain_dir.name}.pkl"
    )

    print(f"✅ Trained replacement model for domain: {domain_dir.name}")
