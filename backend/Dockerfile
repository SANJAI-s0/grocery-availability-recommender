FROM python:3.12-slim

# -----------------------------
# System setup
# -----------------------------
WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends curl \
 && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Python dependencies
# -----------------------------
COPY requirements.txt .
RUN pip install \
    --no-cache-dir \
    --default-timeout=300 \
    --retries=10 \
    -r requirements.txt

# -----------------------------
# Copy backend source
# -----------------------------
COPY . .

# -----------------------------
# Runtime
# -----------------------------
EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://127.0.0.1:5000/health || exit 1

CMD ["python", "app.py"]
