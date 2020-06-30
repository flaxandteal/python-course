from ..models.substance import Substance

class NotEnoughSubstancesToMixException(Exception):
    pass

class UnknownProcessException(Exception):
    pass


MIXTURES = {
    ('Mercury', 'Salt', 'Sulphur'): 'Gloop'
}


class Alembic:
    _nature_of_unknown_mixture = 'Sludge'

    @staticmethod
    def _produce(nature):
        return Substance(nature=nature)

    def mix(self, *substances):
        if len(substances) < 2:
            raise NotEnoughSubstancesToMixException()

        constituents = [substance.nature for substance in substances]

        # This gives us a canonical, ordered way of expressing our
        # constituents that we can use as a recipe look-up
        ingredient_list = tuple(sorted(constituents))

        try:
            nature = MIXTURES[ingredient_list]
        except KeyError:
            nature = self._nature_of_unknown_mixture

        return self._produce(nature)

    def process(self, process_name, substance):
        if process_name == 'ferment':
            result = substance.ferment()
        elif process_name == 'cook':
            result = substance.cook()
        elif process_name == 'wash':
            result = substance.wash()
        elif process_name == 'pickle':
            result = substance.pickle()
        else:
            raise UnknownProcessException()

        return result
