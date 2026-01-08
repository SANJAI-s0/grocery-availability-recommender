import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # backend/
MODEL_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

products = [
    "Whole Milk",
    "Skim Milk",
    "Almond Milk",
    "Brown Bread",
    "White Bread"
]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(products)
similarity_matrix = cosine_similarity(vectors)

model_path = os.path.join(MODEL_DIR, "replacement_model.pkl")
joblib.dump((vectorizer, similarity_matrix, products), model_path)

print(f"Replacement model saved at: {model_path}")
