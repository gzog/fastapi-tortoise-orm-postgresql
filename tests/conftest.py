import pytest
from httpx import AsyncClient
from tortoise import Tortoise

from backend.main import app

DB_URL = "sqlite://:memory:"


async def init_db(db_url) -> None:
    """Initial database connection"""
    await Tortoise.init(
        db_url=db_url, modules={"models": ["backend.models"]}, _create_db=True
    )
    await Tortoise.generate_schemas()


async def init(db_url: str = DB_URL):
    await init_db(db_url)


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        print("Client is ready")
        yield client


@pytest.fixture(scope="session", autouse=True)
async def initialize_tests():
    await init()
    yield
    await Tortoise._drop_databases()
