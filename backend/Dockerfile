# backend/Dockerfile - production-friendly
FROM python:3.12-slim

WORKDIR /app
COPY . .

# install curl for healthcheck and necessary binaries
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# simple healthcheck using the /health endpoint
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://127.0.0.1:5000/health || exit 1

# Run with gunicorn (bind to 0.0.0.0). Adjust workers if needed.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "2", "--threads", "4"]
