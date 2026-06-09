from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_usage_record():
    payload = {
        "provider": "OpenAI",
        "model_name": "gpt-5",
        "input_tokens": 100,
        "output_tokens": 50,
        "total_tokens": 150,
        "cost": 0.01,
        "request_count": 1
    }

    response = client.post(
        "/api/v1/usage/",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["provider"] == "OpenAI"
    assert data["model_name"] == "gpt-5"