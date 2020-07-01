class Pantry:
    _cupboard = []

    def __init__(self):
        pass

    def add_substance(self, substance):
        self._cupboard.append(substance)

    def find_substances_by_nature(self, nature):
        return [substance for substance in self._cupboard if substance.nature == nature]

    def count_all_substances(self):
        return len(self._cupboard)
