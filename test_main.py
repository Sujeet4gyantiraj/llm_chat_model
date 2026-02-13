import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_ask_with_all_fields():
    payload = {
        "query": "How do I reset my password?",
        "system_prompt": "You are a technical support assistant for XYZ Corp",
        "metadata": {"user_id": "12345", "tier": "premium"},
        "context": [1, 2, 3],
        "temperature": 0.7,
        "top_k": 40,
        "top_p": 0.9
    }
    response = client.post("/ask", json=payload)
    assert response.status_code == 200
    assert "response" in response.json()

def test_ask_with_defaults():
    response = client.post("/ask", json={})
    assert response.status_code == 200
    assert "response" in response.json()
