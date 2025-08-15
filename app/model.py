import os
try:
    import joblib
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
except Exception:
    # sklearn or joblib may be unavailable in this environment; we'll fall back
    joblib = None

ARTIFACT_MODEL = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'artifacts', 'model.joblib'))
ARTIFACT_VECT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'artifacts', 'vect.joblib'))


import re
class FallbackModel:
    """Improved fallback classifier: combines keyword, text length, and punctuation features."""
    def __init__(self):
        self.classes_ = ['fake', 'real']
        self.fake_tokens = set([
            'miracle', 'cure', 'secret', 'doctors', 'pill', 'weight', 'stunned', 'alien', 'aliens', 'proves', 'shocking', 'exclusive', 'banned', 'scandal', 'vote', 'pyramids', 'extraterrestrials', 'cats', 'dogs', 'allowed', 'commission', 'revealed', 'nationwide', 'waiting list'
        ])
    def predict_proba(self, X):
        out = []
        for text in X:
            t = (text or '').lower()
            score = 0.0
            # keyword feature
            for tok in self.fake_tokens:
                if tok in t:
                    score += 1.0
            # length feature
            length = len(t)
            score += min(2.0, length/120)
            # punctuation feature
            exclam = t.count('!')
            score += 0.5 * exclam
            # suspicious punctuation
            score += 0.2 * len(re.findall(r'[?]', t))
            # cap feature
            caps = sum(1 for c in text if c.isupper())
            score += min(1.0, caps/20)
            # base probability: more features -> more fake probability
            fake_p = min(0.98, 0.12 + 0.18 * score)
            real_p = 1.0 - fake_p
            out.append([fake_p, real_p])
        return out


class DummyVectorizer:
    def transform(self, X):
        # passthrough; FallbackModel expects raw text iterable
        return X


def load_artifacts():
    """Try to load joblib artifacts; if missing, return pure-Python fallbacks so the API stays usable."""
    if joblib and os.path.exists(ARTIFACT_MODEL) and os.path.exists(ARTIFACT_VECT):
        model = joblib.load(ARTIFACT_MODEL)
        vect = joblib.load(ARTIFACT_VECT)
        return model, vect
    # fallback
    return FallbackModel(), DummyVectorizer()


def predict_text(model, vect, text: str):
    # If vect is a sklearn vectorizer, transform returns sparse array; if DummyVectorizer, it returns raw list
    try:
        x = vect.transform([text])
    except Exception:
        x = [text]
    # model.predict_proba should accept iterable of texts or matrix
    proba_all = model.predict_proba(x)
    proba = proba_all[0]
    # find index of max probability
    # avoid importing numpy here to keep fallback free of binary deps
    idx = int(max(range(len(proba)), key=lambda i: proba[i]))
    label = model.classes_[idx]
    return label, float(proba[idx])
