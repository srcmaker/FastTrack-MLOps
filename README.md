# 🚀 FastTrack-MLOps

A fast-track end-to-end MLOps demo project that showcases the complete lifecycle of a machine learning model — from training and serving to monitoring and CI/CD automation.

---

## 📌 Features

- ✅ Linear regression model with `scikit-learn`
- ✅ FastAPI-based REST inference API
- ✅ Dockerized deployment
- ✅ GitHub Actions for CI/CD pipeline
- ✅ Prometheus integration for metrics monitoring
- ✅ Grafana dashboard ready
- ✅ Modular, minimal, and extensible codebase

---

## 🧱 Project Structure

```
mlops-demo/
├── api/                # FastAPI app for model inference
├── src/                # Model training and prediction scripts
├── model/              # Saved model artifact
├── monitoring/         # Prometheus & Grafana config
├── .github/workflows/  # GitHub Actions CI/CD pipeline
├── Dockerfile          # Container spec
├── requirements.txt    # Python dependencies
├── architecture.md     # System architecture documentation
├── README.md           # Project documentation
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. 🔧 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Train the model
python src/train.py

# Start API server
uvicorn api.app:app --reload
```

### 2. 🔍 Test the API

```bash
curl "http://localhost:8000/predict?x=10"
```

---

## 🐳 Docker Deployment

```bash
# Build the Docker image
docker build -t fasttrack-mlops .

# Run the container
docker run -p 8000:8000 fasttrack-mlops
```

---

## 🔁 CI/CD with GitHub Actions

- Every push to `main`:
  - Installs dependencies
  - Trains model
  - Runs prediction test
  - Builds Docker image
  - Starts container and verifies the API
  - Tears down container

Workflow: `.github/workflows/ci-cd.yml`

---

## 📊 Monitoring

- The FastAPI app exposes metrics at `/metrics` using Prometheus format.
- Prometheus is configured to scrape this endpoint every 15 seconds.
- You can plug Prometheus into Grafana and import `monitoring/grafana-dashboard.json`.

---

## 🧠 Author & Purpose

This project was built as a short-term hands-on portfolio to demonstrate core MLOps skills including:
- Model packaging and deployment
- API development
- Infrastructure automation
- Observability and monitoring

Perfect for use in job applications or team knowledge sharing.

---

## 📃 License

MIT License
