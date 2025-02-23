import pytest
from httpx import AsyncClient
from main import app


@pytest.mark.asyncio
async def test_set_and_get():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/set/", json={"key": "test", "value": "123"})
        assert response.status_code == 200

        response = await ac.get("/get/test")
        assert response.status_code == 200
        assert response.json()["value"] == "123"

@pytest.mark.asyncio
async def test_set_and_get_rdb():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/set/", json={"key": "rdb_test", "value": "123"})
        assert response.status_code == 200

        response = await ac.get("/get/rdb_test")
        assert response.status_code == 200
        assert response.json()["value"] == "123"

@pytest.mark.asyncio
async def test_set_and_get_aof():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/set/", json={"key": "aof_test", "value": "456"})
        assert response.status_code == 200

        response = await ac.get("/get/aof_test")
        assert response.status_code == 200
        assert response.json()["value"] == "456"
