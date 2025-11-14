import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_register_returns_token(client):
    url = reverse("accounts:register")
    payload = {
        "username": "newuser",
        "email": "new@example.com",
        "password": "secret123",
    }
    response = client.post(url, payload)
    assert response.status_code == 201
    assert "token" in response.json()
