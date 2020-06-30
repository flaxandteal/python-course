from flask_restful import Api
from . import substance
from . import alembic_instruction

def init_app(app):
    api = Api(app)
    substance.init_app(app, api)
    alembic_instruction.init_app(app, api)
