import pytest

from magnumopus.repositories.list_pantry import ListPantry
from magnumopus.models.substance import Substance

@pytest.fixture
def list_pantry():
    return ListPantry()

@pytest.fixture
@pytest.mark.asyncio
def pantries(list_pantry):
    return {
        'list': list_pantry
    }

# We may want other pantry-specific tests, but bear in mind LSP
@pytest.mark.parametrize('pantry_type', ['list'])
def test_can_add_to_pantry(pantry_type, pantries):
    pantry = pantries[pantry_type]

    substance = Substance()

    pantry.add_substance(substance)

    assert pantry.count_all_substances() == 1

@pytest.mark.parametrize('pantry_type', ['list'])
def test_can_retrieve_substance_from_pantry_by_nature(pantry_type, pantries):
    pantry = pantries[pantry_type]

    substance = Substance(nature='Mercury')

    pantry.add_substance(substance)

    mercury = pantry.find_substances_by_nature('Mercury')[0]

    assert mercury.nature == 'Mercury'
