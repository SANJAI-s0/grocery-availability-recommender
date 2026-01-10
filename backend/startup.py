# backend/startup.py
import subprocess

DOMAINS = ["grocery", "electronics", "accessories"]

print("🚀 Auto-training models on startup")

for domain in DOMAINS:
    subprocess.run(["python", "backend/utils/preprocess.py", domain], check=True)
    subprocess.run(["python", "backend/ml/train_availability.py", domain], check=True)
    subprocess.run(["python", "backend/ml/train_replacement.py", domain], check=True)

print("✅ All domain models trained")
