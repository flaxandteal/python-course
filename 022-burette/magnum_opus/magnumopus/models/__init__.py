from .base import db
from flask_sqlalchemy import SQLAlchemy

def init_app(app):
    db.init_app(app)
    return [configure_injector]

def configure_injector(binding):
    binding.bind(
        SQLAlchemy, to=db
    )
