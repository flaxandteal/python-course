class ListPantry:
    def __init__(self):
        self._cupboard = []

    def empty_pantry(self):
        self._cupboard = []

    def add_substance(self, substance):
        self._cupboard.append(substance)

    def find_substances_by_nature(self, nature):
        return [substance for substance in self._cupboard if substance.nature == nature]

    def count_all_substances(self):
        return len(self._cupboard)

    def commit(self):
        # Give each substance an ID, if it does not have one
        free_ids = iter(
            set(range(1, len(self._cupboard) + 1)) -
            set([substance.id for substance in self._cupboard if substance])
        )

        for substance in self._cupboard:
            if not substance.id:
                substance.id = next(free_ids)
