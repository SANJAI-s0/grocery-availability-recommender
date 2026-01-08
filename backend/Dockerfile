FROM python:3.12-slim

WORKDIR /app
COPY . .

# install curl for healthcheck and necessary binaries
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# simple healthcheck using the /health endpoint
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://127.0.0.1:5000/health || exit 1

CMD ["python", "app.py"]
