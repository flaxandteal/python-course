from flask_restful import Resource, reqparse
from injector import inject
from ..repositories.pantry import Pantry
from ..models.substance import Substance
from ..schemas.substance_schema import SubstanceSchema
from ..services.alembic_instruction_handler import AlembicInstructionHandler, AlembicInstruction

class AlembicInstructionResource(Resource):
    @inject
    def __init__(self, pantry: Pantry, substance_schema: SubstanceSchema, parser_fcty=reqparse.RequestParser):
        super(AlembicInstructionResource, self).__init__()

        self._pantry = pantry
        self._substance_schema = substance_schema
        self._parser_fcty = parser_fcty

    def get(self):
        """This should return past requests/commands."""
        pass

    def post(self):
        """
        Add an instruction for the alembic.

        Note that POST is _not_ assumed to be idempotent, unlike PUT
        """

        parser = self._parser_fcty()
        parser.add_argument('instruction_type')
        parser.add_argument('action')
        parser.add_argument('natures')

        args = parser.parse_args()
        instruction_type = args['instruction_type']

        pantry = self._pantry

        instruction_handler = AlembicInstructionHandler()

        # This could do with deserialization...
        instruction = AlembicInstruction(
            instruction_type=args.instruction_type,
            natures=args.natures.split(','),
            action=args.action
        )

        # Crude start at DI... see flask-injector
        result = instruction_handler.handle(instruction, pantry)
        print('y', result.state, result.id, self._substance_schema.dump(result))

        pantry.add_substance(result)
        print('z', result.state, result.id, self._substance_schema.dump(result))

        pantry.commit()
        print('a', result.state, result.id, self._substance_schema.dump(result))
        print(result.state, result.id, self._substance_schema.dump(result))

        return self._substance_schema.dump(result), 201


def init_app(app, api):
    api.add_resource(AlembicInstructionResource, '/alembic_instruction')
