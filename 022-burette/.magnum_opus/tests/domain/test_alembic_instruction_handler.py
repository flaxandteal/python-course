import pytest

from magnumopus.services.alembic_instruction_handler import AlembicInstruction, AlembicInstructionHandler
from magnumopus.repositories.list_pantry import ListPantry
from magnumopus.models.substance import Substance

@pytest.fixture
def instruction_unknown():
    return AlembicInstruction(
        'saute',
        ['Sulphur'],
        'cook'
    )

@pytest.fixture
def instruction():
    return AlembicInstruction(
        'process',
        ['Sludge'],
        'cook'
    )

@pytest.fixture
def pantry():
    pantry = ListPantry()

    substance = Substance(nature='Sludge')
    pantry.add_substance(substance)

    substance = Substance(nature='Sulphur')
    pantry.add_substance(substance)

    return pantry

def test_can_set_up_my_alembic_instruction_handler(instruction, pantry):
    handler = AlembicInstructionHandler()
    handler.handle(instruction, pantry)
