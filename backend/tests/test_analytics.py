from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_dashboard_endpoint(client):
    response = client.get("/api/v1/analytics/dashboard")

    assert response.status_code == 200

    data = response.json()

    assert "summary" in data
    assert "providers" in data
    assert "models" in data
    assert "trends" in data