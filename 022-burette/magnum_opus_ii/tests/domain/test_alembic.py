import pytest

from magnumopus.services.alembic import Alembic, NotEnoughSubstancesToMixException, UnknownProcessException
from magnumopus.models.substance import Substance

def test_can_set_up_my_alembic():
    Alembic()

def test_can_mix_multiple_substances_in_my_alembic():
    alembic = Alembic()
    substance = [Substance() for _ in range(3)]
    alembic.mix(*substance)

    substance = [Substance() for _ in range(6)]
    alembic.mix(*substance)

def test_cannot_mix_one_substance_in_my_alembic():
    alembic = Alembic()
    substance = Substance()

    with pytest.raises(NotEnoughSubstancesToMixException):
        alembic.mix(substance)

def test_mixing_sulphur_salt_and_mercury_gives_gloop():
    alembic = Alembic()

    sulphur = Substance(nature='Sulphur')
    salt = Substance(nature='Salt')
    mercury = Substance(nature='Mercury')

    result = alembic.mix(sulphur, salt, mercury)

    assert result.nature == 'Gloop'

    result = alembic.mix(mercury, sulphur, salt)

    assert result.nature == 'Gloop'

def test_mixing_other_recipes_gives_sludge():
    alembic = Alembic()

    sulphur = Substance(nature='Sulphur')
    salt = Substance(nature='Salt')
    mercury = Substance(nature='Mercury')
    gloop = Substance(nature='Gloop')

    result = alembic.mix(sulphur, salt, mercury, sulphur)

    assert result.nature == 'Sludge'

    result = alembic.mix(salt, mercury)

    assert result.nature == 'Sludge'

    result = alembic.mix(gloop, salt, mercury)

    assert result.nature == 'Sludge'

def test_can_process_substance():
    alembic = Alembic()

    substance = Substance()
    result = alembic.process('cook', substance)

    substance = Substance()
    cooked_substance = substance.cook()

    assert result.state == cooked_substance.state

    result = alembic.process('ferment', substance)
    cooked_fermented_substance = cooked_substance.ferment()

    assert result.state == cooked_fermented_substance.state

def test_cannot_perform_unknown_process():
    alembic = Alembic()

    substance = Substance()

    with pytest.raises(UnknownProcessException):
        alembic.process('boil', substance)
