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
