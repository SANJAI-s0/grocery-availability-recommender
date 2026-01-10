# 📦 Changelog

All notable changes to this project will be documented in this file.

This project follows a **semester-based milestone model** rather than strict semantic versioning.

---

## [Unreleased]

### Added
- Domain-aware machine learning models (grocery, electronics, accessories)
- Automatic preprocessing for all domains on container startup
- Automatic ML model training on container startup
- Availability badge (Available / Out of Stock)
- Sales vs Availability visualization chart
- Similarity-based replacement recommendations using TF-IDF + cosine similarity
- Domain selector in frontend UI
- GitHub Actions CI pipeline

### Changed
- Replaced random replacement logic with similarity-based recommendations
- Updated API to support multi-domain datasets
- Improved frontend state management for availability & replacements
- Backend model loading now supports per-domain models with fallback

### Fixed
- Product name mismatch issues in availability prediction
- Frontend domain switching bugs
- Docker startup ordering issues between preprocessing and training

---

## [2026-01-10] – End-Semester Submission

### Added
- Full-stack React + Flask application
- Dockerized frontend and backend
- Initial ML availability prediction
- Replacement recommendation system
- REST APIs with health checks

### Notes
- Academic demonstration release
- Models intentionally lightweight for explainability
