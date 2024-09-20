from fastapi.testclient import TestClient
from mini_groq import app

client = TestClient(app)

# Test de l'endpoint /status
def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
