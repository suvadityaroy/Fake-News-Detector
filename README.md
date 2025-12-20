# 🔍 Fake News Detector

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)

> AI-powered detection system for identifying misinformation in news articles

🔗 **[Live Demo](https://fake-news-detector.up.railway.app)** • 📚 **[API Docs](https://fake-news-detector.up.railway.app/docs)**

## ✨ Features

- 🤖 ML-powered fake news detection
- 📄 Multi-format support (text, PDF, DOCX, TXT)
- 📊 Confidence scoring with visual bars
- 🌍 Auto language detection
- 💾 Export as PDF / 📤 Share results
- 🎨 Modern animated UI
- ⚡ REST API with full documentation

## 🛠️ Tech Stack

**Backend:** Python, FastAPI, scikit-learn, pandas, joblib  
**Frontend:** HTML5, CSS3, JavaScript (ES6+)  
**Deployment:** Railway, Uvicorn  

## 🚀 Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/suvadityaroy/Fake-News-Detector.git
cd Fake-News-Detector
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate      # macOS/Linux
pip install -r requirements.txt
```

### 2. Train Model
```bash
python train.py
```

### 3. Run Server
```bash
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

### 4. Access
- 🌐 Web UI: [http://127.0.0.1:8000/static/](http://127.0.0.1:8000/static/)
- 📚 API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/predict` | Analyze text for fake/real news |
| `POST` | `/extract` | Extract text from file |
| `GET` | `/health` | Health check |

## 👨‍💻 Created by

**Suvaditya Roy** — [GitHub](https://github.com/suvadityaroy) | [LinkedIn](https://linkedin.com/in/suvadityaroy)