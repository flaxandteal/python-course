from . import substance
from . import alembic_instruction

def init_app(app):
    substance.init_app(app)
    alembic_instruction.init_app(app)
    return []
