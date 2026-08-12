import uuid

def test_create_usage_record(client):

    unique_id = uuid.uuid4().hex[:8]

    email = f"usage_{unique_id}@test.com"
    username = f"usage_{unique_id}"

    # Register user
    register_payload = {
        "email": email,
        "username": username,
        "password": "password123"
    }

    client.post(
        "/api/v1/auth/register",
        json=register_payload
    )

    # Login
    login_payload = {
        "email": email,
        "password": "password123"
    }

    login_response = client.post(
        "/api/v1/auth/login",
        json=login_payload
    )

    assert login_response.status_code == 200

    token = login_response.json()["data"]["access_token"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

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
        json=payload,
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True