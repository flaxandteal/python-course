class SubstanceMustBeFreshToProcessException(Exception):
    pass

class Substance:
    def __init__(self, nature='Unknown'):
        self.nature = nature
        self.state = []

    def _process(self, process_name):
        self.state.append(process_name)
        return self

    def cook(self):
        return self._process('cooked')

    def pickle(self):
        return self._process('pickled')

    def ferment(self):
        return self._process('fermented')

    def wash(self):
        return self._process('washed')
