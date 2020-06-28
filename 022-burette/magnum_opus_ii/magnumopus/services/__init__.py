from .alembic import Alembic

def init_app(app):
    return [configure_injector]

def configure_injector(binder):
    binder.bind(
        Alembic, to=Alembic
    )
