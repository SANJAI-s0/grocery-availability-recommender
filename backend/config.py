import os

DB_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///grocery.db"  # default for local dev
)

MODEL_PATH = "models/"
