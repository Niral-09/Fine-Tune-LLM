import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_get_answer():
    response = client.post("/qa/", json={"context": "Hello world", "question": "What is this?"})
    assert response.status_code == 200
    assert "answer" in response.json()
    assert "score" in response.json()
