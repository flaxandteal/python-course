from magnumopus.pantry import Pantry
from magnumopus.substance import Substance

def test_can_add_to_pantry():
    pantry = Pantry()

    substance = Substance()

    pantry.add_substance(substance)

    assert pantry.count_all_substances() == 1

def test_can_retrieve_substance_from_pantry_by_nature():
    pantry = Pantry()

    substance = Substance(nature='Mercury')

    pantry.add_substance(substance)

    mercury = pantry.find_substance_by_nature('Mercury')

    assert mercury.nature == 'Mercury'
