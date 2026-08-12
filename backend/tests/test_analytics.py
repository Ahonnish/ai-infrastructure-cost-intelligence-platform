import uuid

def test_dashboard_endpoint(client):

    unique_id = uuid.uuid4().hex[:8]

    email = f"analytics_{unique_id}@test.com"
    username = f"analytics_{unique_id}"

    register_payload = {
        "email": email,
        "username": username,
        "password": "password123"
    }

    client.post(
        "/api/v1/auth/register",
        json=register_payload
    )

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

    response = client.get(
        "/api/v1/analytics/dashboard",
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()

    assert "summary" in data
    assert "providers" in data
    assert "models" in data
    assert "trends" in data