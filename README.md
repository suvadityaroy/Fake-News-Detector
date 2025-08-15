
# Fake News Detector

A minimal web app and API for detecting fake news headlines or articles using machine learning.

## What It Does
- Detects whether a news headline or short article is likely fake or real.
- Accepts direct text input or file upload (PDF, Word, TXT).
- Shows probability/confidence and a simple explanation.
- Detects language automatically.
- Allows saving results as PDF or sharing.
- Animated, modern UI (PWA-ready for install on mobile/desktop).

## Skills & Technologies Used
- **Python** (FastAPI, scikit-learn, pandas, joblib)
- **Frontend**: HTML, CSS, JavaScript (animated UI, file upload, browser APIs)
- **File extraction**: PyPDF2, python-docx
- **API**: REST endpoints for prediction, extraction, health check
- **Testing**: pytest

## How to Use

### 1. Install Requirements
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Train the Model
```powershell
python train.py
```

### 3. Start the Server
```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

### 4. Use the App
- Open [http://127.0.0.1:8000/static/](http://127.0.0.1:8000/static/) in your browser for the web UI.
- Try the API docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive API testing.

### 5. Features
- Paste or upload news text, click Detect.
- See result, probability, explanation, and detected language.
- Save as PDF or share result.
- Works as a PWA (installable from browser menu).

## Attribution
**Created by Suvaditya Roy**

---
For demo purposes only. Not for production use. Improve with more data and robust validation for real-world deployment.
