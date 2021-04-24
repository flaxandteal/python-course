from . import db
import uuid
from sqlalchemy_utils import ScalarListType

class SubstanceMustBeFreshToProcessException(Exception):
    pass


class Substance(db.Model):
    id = db.columns.UUID(primary_key=True, default=uuid.uuid4)
    nature = db.columns.Text()
    state = db.columns.List(db.columns.Text())

    def __init__(self, nature='Unknown'):
        super(Substance, self).__init__(nature=nature, state=[])

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
