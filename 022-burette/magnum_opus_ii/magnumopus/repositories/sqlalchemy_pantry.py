from flask_sqlalchemy import SQLAlchemy
from injector import inject

from ..models.substance import Substance
from ..models import db

class SQLAlchemyPantry:
    @inject
    def __init__(self, db: SQLAlchemy):
        self._db = db

    def empty_pantry(self):
        Substance.query.delete()

    # A more involved solution would open and close the pantry... like
    # a cupboard door, or a Unit of Work

    # Note how we're committing too frequently?
    def add_substance(self, substance):
        self._db.session.add(substance)
        return substance

    def find_substances_by_nature(self, nature):
        substances = Substance.query.filter_by(nature=nature).all()
        return substances

    def count_all_substances(self):
        return Substance.query.count()

    def commit(self):
        self._db.session.commit()
