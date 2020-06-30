from flask_restful import Resource, reqparse
from ..repositories.pantry import Pantry
from ..repositories.sqlalchemy_pantry import SQLAlchemyPantry
from ..models import db
from ..models.substance import Substance
from ..schemas.substance_schema import SubstanceSchema

parser = reqparse.RequestParser()
parser.add_argument('nature')

substance_schema = SubstanceSchema()
substances_schema = SubstanceSchema(many=True)

pantry_cls = SQLAlchemyPantry


class SubstanceResource(Resource):
    def get(self):
        args = parser.parse_args()
        nature = args['nature']

        pantry = pantry_cls()

        substances = pantry.find_substances_by_nature(nature)

        return substances_schema.dump(substances)

    def post(self):
        args = parser.parse_args()
        nature = args['nature']

        pantry = pantry_cls()

        substance = Substance(nature=nature)

        pantry.add_substance(substance)

        pantry.commit()

        return substance_schema.dump(substance)


def init_app(app, api):
    api.add_resource(SubstanceResource, '/substance')
