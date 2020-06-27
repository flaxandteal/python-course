from dataclasses import dataclass
from injector import inject

from .alembic import Alembic
from ..repositories.pantry import Pantry

class UnknownAlembicInstructionException(Exception):
    pass

@dataclass
class AlembicInstruction:
    instruction_type: str
    natures: list
    action: str = ''

class AlembicInstructionHandler:
    @inject
    def handle(self, instruction: AlembicInstruction, pantry: Pantry):
        natures = instruction.natures
        action = instruction.action
        instruction_type = instruction.instruction_type

        # Clearly need some validation here!
        substances = [pantry.find_substances_by_nature(nature)[0] for nature in natures]

        alembic = Alembic()

        if instruction_type == 'mix':
            result = alembic.mix(*substances)
        elif instruction_type == 'process':
            result = alembic.process(action, substances[0])
        else:
            raise UnknownAlembicInstructionException(f'Unknown instruction: {action}')

        return result
