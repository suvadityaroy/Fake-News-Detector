"""Train a simple TF-IDF + LogisticRegression fake news model using the sample CSV and save artifacts."""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
import joblib
import os

ROOT = os.path.dirname(__file__)
DATA = os.path.join(ROOT, 'data', 'sample.csv')
ART_DIR = os.path.join(ROOT, 'artifacts')
MODEL_PATH = os.path.join(ART_DIR, 'model.joblib')
VECT_PATH = os.path.join(ART_DIR, 'vect.joblib')


def train(save=True):
    df = pd.read_csv(DATA)
    X = df['text'].fillna('')
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    vect = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
    Xt = vect.fit_transform(X_train)
    model = LogisticRegression(max_iter=1000)
    model.fit(Xt, y_train)

    if save:
        os.makedirs(ART_DIR, exist_ok=True)
        joblib.dump(model, MODEL_PATH)
        joblib.dump(vect, VECT_PATH)
        print(f"Saved model -> {MODEL_PATH}")
    return model, vect


if __name__ == '__main__':
    train()
