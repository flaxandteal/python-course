from quart import request
from quart_openapi import Resource
from injector import inject
from ..injection import ViewInjectorMeta
from ..repositories.pantry import Pantry
from ..models.substance import Substance
from ..schemas.substance_schema import SubstanceSchema
from ..services.alembic_instruction_handler import AlembicInstructionHandler, AlembicInstruction

class AlembicInstructionResource(Resource):
    @inject
    def __init__(self, pantry: Pantry, substance_schema: SubstanceSchema):
        super(AlembicInstructionResource, self).__init__()

        self._pantry = pantry
        self._substance_schema = substance_schema

    async def get(self):
        """This should return past requests/commands."""
        pass

    async def post(self):
        """
        Add an instruction for the alembic.

        Note that POST is _not_ assumed to be idempotent, unlike PUT
        """

        args = await request.get_json()

        instruction_type = args['instruction_type']

        pantry = self._pantry

        instruction_handler = AlembicInstructionHandler()

        # This could do with deserialization...
        instruction = AlembicInstruction(
            instruction_type=args['instruction_type'],
            natures=args['natures'].split(','),
            action=args['action'] if 'action' in args else ''
        )

        result = instruction_handler.handle(instruction, pantry)

        pantry.add_substance(result)

        pantry.commit()

        return self._substance_schema.dump(result), 201


def init_app(app):
    class AppAlembicInstructionResource(AlembicInstructionResource, metaclass=ViewInjectorMeta):
        get_app = lambda: app

    app.route('/alembic_instruction', endpoint='alembic_instruction')(AppAlembicInstructionResource)
