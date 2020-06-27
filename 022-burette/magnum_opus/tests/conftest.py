import pytest
from magnumopus import create_app
from magnumopus.models import db

@pytest.fixture(scope='session')
def app():
    app = create_app()
    return app


@pytest.fixture(scope='session')
def _db(app):
    with app.app_context():
        db.create_all()
    return db

@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
    db.drop_all()
