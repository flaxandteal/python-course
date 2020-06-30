class Pantry:
    def __init__(self):
        self._cupboard = []

    def add_substance(self, substance):
        self._cupboard.append(substance)

    def find_substance_by_nature(self, nature):
        return [substance for substance in self._cupboard if substance.nature == nature][0]

    def count_all_substances(self):
        return len(self._cupboard)
