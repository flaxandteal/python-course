from .base import db
from flask_cqlalchemy import CQLAlchemy


def init_app(app):
    db.init_app(app)
    return [configure_injector]

def configure_injector(binding):
    binding.bind(
        CQLAlchemy, to=db
    )
