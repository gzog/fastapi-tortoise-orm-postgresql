import pytest
from httpx import AsyncClient

from app.user.models import User


@pytest.mark.anyio
async def test_create_user(client: AsyncClient):
    payload = {
        "username": "admin",
        "name": "George",
        "family_name": "Test",
        "password": "admin",
    }
    response = await client.post("/users", json=payload)
    assert response.status_code == 200, response.text

    data = response.json()

    assert "id" in data
    assert data["username"] == "admin"
    assert data["name"] == "George"
    assert data["family_name"] == "Test"

    user_id = data["id"]
    user = await User.get(id=user_id)
    assert user.verify_password(payload["password"])
    assert user.id == user_id
