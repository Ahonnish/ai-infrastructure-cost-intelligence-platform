import uuid


def register_and_login(client):
    unique_id = uuid.uuid4().hex[:8]

    register_payload = {
        "email": f"user_{unique_id}@test.com",
        "username": f"user_{unique_id}",
        "password": "password123"
    }

    register_response = client.post(
        "/api/v1/auth/register",
        json=register_payload
    )

    assert register_response.status_code == 200

    login_response = client.post(
        "/api/v1/auth/login",
        json={
            "email": register_payload["email"],
            "password": register_payload["password"]
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()["data"]["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }


def create_usage_record(
    client,
    headers,
    provider,
    model_name,
    cost,
    tokens
):
    payload = {
        "provider": provider,
        "model_name": model_name,
        "input_tokens": tokens // 2,
        "output_tokens": tokens // 2,
        "total_tokens": tokens,
        "cost": cost,
        "request_count": 1
    }

    response = client.post(
        "/api/v1/usage/",
        json=payload,
        headers=headers
    )

    assert response.status_code == 200


def test_multi_tenant_isolation(client):
    # User A
    headers_a = register_and_login(client)

    create_usage_record(
        client,
        headers_a,
        "OpenAI",
        "gpt-4o",
        0.01,
        200
    )

    create_usage_record(
        client,
        headers_a,
        "Gemini",
        "gemini-2.5-pro",
        0.02,
        400
    )

    # User B
    headers_b = register_and_login(client)

    create_usage_record(
        client,
        headers_b,
        "Anthropic",
        "claude-4",
        0.03,
        600
    )

    # Analytics for User A
    response_a = client.get(
        "/api/v1/analytics/summary",
        headers=headers_a
    )

    assert response_a.status_code == 200

    summary_a = response_a.json()

    assert summary_a["total_cost"] == 0.03
    assert summary_a["total_tokens"] == 600
    assert summary_a["total_requests"] == 2

    # Analytics for User B
    response_b = client.get(
        "/api/v1/analytics/summary",
        headers=headers_b
    )

    assert response_b.status_code == 200

    summary_b = response_b.json()

    assert summary_b["total_cost"] == 0.03
    assert summary_b["total_tokens"] == 600
    assert summary_b["total_requests"] == 1