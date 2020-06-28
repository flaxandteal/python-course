import pytest
from magnumopus import create_app
from magnumopus.repositories.pantry import Pantry

@pytest.fixture
async def app():
    app = create_app()
    await app.startup()
    yield app
    await app.shutdown()


@pytest.fixture
async def client(app):
    pantry = app.extensions['injector'].get(Pantry)
    pantry.empty_pantry()
    async with app.test_client() as client:
        yield client
    pantry.empty_pantry()
