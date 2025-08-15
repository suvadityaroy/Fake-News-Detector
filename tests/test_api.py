import os
from fastapi.testclient import TestClient
from app import main

client = TestClient(main.app)

def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json().get('status') == 'ok'

# optional: run training first then test predict
def test_predict_flow():
    # run training if artifacts missing
    from train import train
    train()
    r = client.post('/predict', json={'text':'Scientists discover vaccine for common cold'})
    assert r.status_code == 200
    data = r.json()
    assert 'label' in data and 'probability' in data
