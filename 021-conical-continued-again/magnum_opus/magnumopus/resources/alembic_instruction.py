from flask_restful import Resource, reqparse
from ..repositories.pantry import Pantry
from ..repositories.sqlalchemy_pantry import SQLAlchemyPantry
from ..models.substance import Substance
from ..schemas.substance_schema import SubstanceSchema
from ..services.alembic_instruction_handler import AlembicInstructionHandler, AlembicInstruction

parser = reqparse.RequestParser()
parser.add_argument('instruction_type')
parser.add_argument('action')
parser.add_argument('natures')

substance_schema = SubstanceSchema()

class AlembicInstructionResource(Resource):
    def get(self):
        """This should return past requests/commands."""
        pass

    def post(self):
        """
        Add an instruction for the alembic.

        Note that POST is _not_ assumed to be idempotent, unlike PUT
        """

        args = parser.parse_args()
        instruction_type = args['instruction_type']

        pantry = SQLAlchemyPantry()

        instruction_handler = AlembicInstructionHandler()

        # This could do with deserialization...
        instruction = AlembicInstruction(
            instruction_type=args.instruction_type,
            natures=args.natures.split(','),
            action=args.action
        )

        # Crude start at DI... see flask-injector
        result = instruction_handler.handle(instruction, pantry)

        pantry.add_substance(result)

        pantry.commit()

        return substance_schema.dump(result)


def init_app(app, api):
    api.add_resource(AlembicInstructionResource, '/alembic_instruction')
