# 🔍 Fake News Detector

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Advanced AI-powered detection system for identifying misinformation and fake news articles with confidence scoring**

🔗 **[✨ Live Demo](https://fake-news-detector.up.railway.app)** • 📚 **[API Documentation](https://fake-news-detector.up.railway.app/docs)**

---

## 📖 What is Fake News Detector?

A sophisticated web application and REST API that leverages machine learning to analyze news content and detect whether articles or headlines are likely to be fake or authentic. The system provides detailed confidence scores, explanations, and metadata to help users make informed decisions about information credibility.

Perfect for journalists, content moderators, researchers, and anyone looking to verify news authenticity.

---

## ✨ Key Features

- 🤖 **AI-Powered Detection**: Advanced machine learning model trained on real/fake news datasets
- 📄 **Multi-Format Support**: Analyze text directly, upload PDF, DOCX, or TXT files
- 📊 **Confidence Scoring**: Get probability percentages with visual confidence bars
- 🌍 **Auto Language Detection**: Automatically detects the language of input text
- 💾 **Export Results**: Save analysis results as PDF for records and documentation
- 📤 **Share Capability**: Easily share detection results with others
- 🎨 **Modern UI**: Beautiful, animated interface with smooth transitions and professional design
- 📱 **Progressive Web App**: Install on mobile devices or desktop for offline functionality
- ⚡ **REST API**: Full-featured API endpoints for integration with other applications
- 🔍 **Detailed Explanations**: Understand why content is flagged as fake or real

---

## 🛠️ Tech Stack & Languages

### Backend
- **Python 3.9+** - Core programming language
- **FastAPI** - Modern, fast web framework for building APIs
- **scikit-learn** - Machine learning library for model training and predictions
- **pandas** - Data manipulation and analysis
- **joblib** - Model serialization and persistence
- **PyPDF2** - PDF file text extraction
- **python-docx** - DOCX file text extraction
- **pytest** - Unit testing framework

### Frontend
- **HTML5** - Semantic markup structure
- **CSS3** - Advanced styling with animations, gradients, and effects
- **JavaScript (ES6+)** - Interactive features, file handling, API communication
- **Service Workers** - PWA capabilities for offline support

### DevOps & Deployment
- **Railway** - Cloud deployment platform
- **Uvicorn** - ASGI web server
- **Git/GitHub** - Version control

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Virtual environment (recommended)

### Step 1️⃣ Clone the Repository
```bash
git clone https://github.com/suvadityaroy/Fake-News-Detector.git
cd Fake-News-Detector
```

### Step 2️⃣ Create & Activate Virtual Environment
```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.\.venv\Scripts\Activate.ps1

# On macOS/Linux
source .venv/bin/activate
```

### Step 3️⃣ Install Dependencies
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4️⃣ Train the ML Model
```powershell
python train.py
```
This will generate trained model files in the `artifacts/` directory.

### Step 5️⃣ Start the Application
```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

### Step 6️⃣ Access the Application
- 🌐 **Web UI**: [http://127.0.0.1:8000/static/](http://127.0.0.1:8000/static/)
- 📚 **API Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- 🔧 **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 💡 Usage Guide

### Via Web Interface
1. ✍️ Paste news text into the text area or upload a file (PDF/DOCX/TXT)
2. 🔍 Click the "**Analyze**" button
3. ⏱️ Wait for analysis to complete
4. 📊 View results with confidence score and explanation
5. 💾 Save as PDF or 📤 share the results

### Via REST API
```bash
# Predict endpoint
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "Your news text here"}'

# Extract text from file
curl -X POST "http://127.0.0.1:8000/extract" \
  -F "file=@document.pdf"

# Health check
curl http://127.0.0.1:8000/health
```

---

## 📂 Project Structure

```
Fake-News-Detector/
├── app/
│   ├── __init__.py           # FastAPI app initialization
│   ├── main.py               # API routes and endpoints
│   └── model.py              # ML model prediction logic
├── artifacts/
│   ├── model.joblib          # Trained model file
│   └── vect.joblib           # TF-IDF vectorizer
├── data/
│   └── sample.csv            # Sample dataset
├── static/
│   ├── index.html            # Web UI
│   ├── manifest.json         # PWA manifest
│   └── sw.js                 # Service worker
├── tests/
│   └── test_api.py           # API tests
├── train.py                  # Model training script
├── requirements.txt          # Python dependencies
├── Procfile                  # Railway deployment config
└── README.md                 # This file
```

---

## 🎓 How It Works

1. **Text Preprocessing**: Input text is cleaned and normalized
2. **Vectorization**: Text is converted to numerical features using TF-IDF
3. **ML Classification**: Trained model classifies as "Real" or "Fake"
4. **Confidence Scoring**: Probability scores indicate model confidence
5. **Result Display**: User-friendly presentation of results with explanations

---

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/predict` | Predict fake/real for given text |
| `POST` | `/extract` | Extract text from uploaded file |
| `GET` | `/health` | Health check endpoint |
| `GET` | `/docs` | Interactive API documentation |

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 🔧 Submit pull requests for improvements
- 📝 Improve documentation

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Created by

**Suvaditya Roy**

- 🔗 [GitHub](https://github.com/suvadityaroy)
- 💼 [LinkedIn](https://linkedin.com/in/suvadityaroy)
- 🌐 [Portfolio](https://suvadityaroy.dev)

---

<div align="center">

### ⭐ If you found this helpful, please consider giving it a star!

**Made with ❤️ using Python, FastAPI, and ML** 🚀

</div>
- Works as a PWA (installable from browser menu).

## Attribution
**Created by Suvaditya Roy**