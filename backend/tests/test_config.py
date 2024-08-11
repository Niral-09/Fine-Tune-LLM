import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_configure_model():
    response = client.post("/config/", json={"model_name": "distilbert-base-uncased-distilled-squad"})
    assert response.status_code == 200
    assert "message" in response.json()