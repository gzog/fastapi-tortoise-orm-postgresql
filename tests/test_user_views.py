# mypy: no-disallow-untyped-decorators
# pylint: disable=E0611,E0401
import pytest
from httpx import AsyncClient

from app.user.models import User


@pytest.mark.anyio
async def test_create_user(client: AsyncClient):
    response = await client.post("/users", json={"username": "admin"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["username"] == "admin"
    assert "id" in data
    user_id = data["id"]

    user_obj = await User.get(id=user_id)
    assert user_obj.id == user_id
