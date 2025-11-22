
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, FileResponse
from pydantic import BaseModel
from app.model import load_artifacts, predict_text
from fastapi.staticfiles import StaticFiles
import os
import tempfile
import io
import sys




app = FastAPI(title="Fake News Detector")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mount static frontend
static_dir = os.path.join(os.path.dirname(__file__), '..', 'static')
if os.path.isdir(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir, html=True), name="static")

class TextRequest(BaseModel):
    text: str

def extract_text_from_file(file: UploadFile):
    ext = file.filename.lower().split('.')[-1]
    content = file.file.read()
    if ext == 'txt':
        try:
            return content.decode(errors='ignore')
        except Exception as e:
            print(f"TXT decode error: {e}", file=sys.stderr)
            return ''
    elif ext == 'pdf':
        try:
            import PyPDF2
            pdf = PyPDF2.PdfReader(io.BytesIO(content))
            text = ''
            for page in pdf.pages:
                text += page.extract_text() or ''
            return text
        except Exception as e:
            print(f"PDF extraction error: {e}", file=sys.stderr)
            return ''
    elif ext == 'docx':
        try:
            import docx
            doc = docx.Document(io.BytesIO(content))
            return '\n'.join([p.text for p in doc.paragraphs])
        except Exception as e:
            print(f"DOCX extraction error: {e}", file=sys.stderr)
            return ''
    print(f"Unsupported file type: {ext}", file=sys.stderr)
    return ''

@app.get('/')
async def root():
    """Redirect root to static frontend"""
    return RedirectResponse(url='/static/index.html')

@app.post('/extract')
async def extract(file: UploadFile = File(...)):
    try:
        text = extract_text_from_file(file)
        if not text:
            return {"text": "", "error": "No text extracted. Check file format or content."}
        return {"text": text}
    except Exception as e:
        print(f"Extraction endpoint error: {e}", file=sys.stderr)
        return {"text": "", "error": str(e)}

@app.get('/health')
async def health():
    return {"status": "ok"}

@app.post('/predict')
async def predict(req: TextRequest):
    if not req.text or not req.text.strip():
        raise HTTPException(status_code=400, detail="text is required")
    model, vect = load_artifacts()
    label, prob = predict_text(model, vect, req.text)
    return {"label": label, "probability": float(prob)}
