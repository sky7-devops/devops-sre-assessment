from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_info():
    response = client.get("/api/info")

    assert response.status_code == 200
    assert response.json()["application"] == "devops-sre-assessment"


def test_not_found():
    response = client.get("/does-not-exist")

    assert response.status_code == 404