import pytest
from httpx import AsyncClient

from app.user.models import User


@pytest.mark.anyio
async def test_create_user(client: AsyncClient):
    payload = {
        "username": "admin",
        "name": "George",
        "family_name": "Test",
    }
    response = await client.post("/users", json=payload)
    assert response.status_code == 200, response.text

    data = response.json()
    assert data["username"] == "admin"
    assert "id" in data

    user_id = data["id"]
    user_obj = await User.get(id=user_id)
    assert user_obj.id == user_id
