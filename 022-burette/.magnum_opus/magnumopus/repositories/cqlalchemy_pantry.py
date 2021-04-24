from flask_cqlalchemy import CQLAlchemy
from injector import inject

from ..models.substance import Substance
from ..models import db

class CQLAlchemyPantry:
    @inject
    def __init__(self, db: CQLAlchemy):
        self._db = db
        self._add_buffer = []

    # A more involved solution would open and close the pantry... like
    # a cupboard door, or a Unit of Work

    # Note how we're committing too frequently?
    def add_substance(self, substance):
        self._add_buffer.append(substance)
        return substance

    def find_substances_by_nature(self, nature):
        substances = Substance.objects().filter(nature=nature).all()
        return substances

    def count_all_substances(self):
        return Substance.objects().count()

    def commit(self):
        for substance in self._add_buffer:
            substance.save()
