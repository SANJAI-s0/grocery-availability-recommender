# 🛒 Grocery Availability Recommender

A full-stack, machine-learning–powered system that predicts grocery item availability and suggests intelligent replacements when items are likely to be out of stock.

This project is inspired by real-world problems faced by online grocery platforms (e.g., Instacart) and is implemented **entirely using free and open-source tools**.

---

## 📌 Problem Statement

In online grocery shopping, items frequently go out of stock.  
This leads to:
- Cart abandonment
- Poor customer experience
- Low acceptance of replacements

### Objective
1. Predict whether a grocery item is likely to be **available or out of stock**
2. Suggest **intelligent replacements** based on similarity and category
3. Deliver the solution as an **end-to-end full-stack product**

---

## 🚀 Features

- 🔮 **Availability Prediction**
  - Uses a machine learning model to predict item availability
- 🔁 **Intelligent Replacement Suggestions**
  - Suggests similar items when the original is unavailable
- 🧠 **ML-Powered Backend**
  - Scikit-learn models for prediction and recommendation
- 🌐 **Full-Stack Application**
  - React frontend + Flask backend
- 🐳 **Dockerized Deployment**
  - Frontend and backend run as containers
- ❤️ **Health Checks**
  - Docker health endpoints for production readiness
- 📦 **Production-Ready Frontend**
  - Nginx-served static React build
  - SEO metadata, manifest, favicon support

---

## 🏗️ System Architecture




---

## 🧰 Tech Stack

### Frontend
- React
- HTML5, CSS3
- Nginx (production serving)

### Backend
- Python 3.12
- Flask + Flask-CORS
- SQLAlchemy
- Scikit-learn

### Database
- SQLite (local)
- PostgreSQL (production-ready)

### DevOps
- Docker
- Docker Compose

---

## 📂 Project Structure




---

## ⚙️ Setup & Installation

### Prerequisites
- Docker
- Docker Compose
- Git

---

### ▶️ Run with Docker (Recommended)

```bash
docker compose up --build
```

**Access the application:**
```
http://localhost:3000        # Frontend
http://localhost:5000        # Backend API
http://localhost:5000/health # Health Check
```

---

### 🔌 API Endpoints
`
| Method | Endpoint                    | Description                 |
| ------ | --------------------------- | --------------------------- |
| GET    | `/`                         | API status                  |
| GET    | `/health`                   | Health check (Docker/Prod)  |
| POST   | `/api/predict-availability` | Predict item availability   |
| POST   | `/api/recommend`            | Get replacement suggestions |
`

---
