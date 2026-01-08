import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Absolute path to backend/models
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # backend/
MODEL_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

# Dummy training data
data = pd.DataFrame({
    "sales": [5, 20, 2, 30, 1],
    "day": [1, 2, 3, 4, 5],
    "available": [1, 0, 1, 0, 1]
})

X = data[["sales", "day"]]
y = data["available"]

model = LogisticRegression()
model.fit(X, y)

# Save model correctly
model_path = os.path.join(MODEL_DIR, "availability_model.pkl")
joblib.dump(model, model_path)

print(f"Availability model saved at: {model_path}")
