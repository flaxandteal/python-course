from . import db
from sqlalchemy_utils import ScalarListType

class SubstanceMustBeFreshToProcessException(Exception):
    pass

class Substance(db.Model):
    __tablename__ = 'substances'

    id = db.Column(db.Integer, primary_key=True)
    nature = db.Column(db.String(32), default='Unknown')
    state = db.Column(ScalarListType())

    def __init__(self, nature='Unknown'):
        self.state = []
        self.nature = nature

        super(Substance, self).__init__()

    def _process(self, process_name):
        # Example of leakage of persistence behaviour into
        # domain, due to db.Model -- we must copy the state list to
        # ensure it is seen to change...
        state = self.state[:]
        state.append(process_name)
        self.state = state

        return self

    def cook(self):
        return self._process('cooked')

    def pickle(self):
        return self._process('pickled')

    def ferment(self):
        return self._process('fermented')

    def wash(self):
        return self._process('washed')
