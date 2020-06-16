from flask_restful import Resource, reqparse
from ..repositories.pantry import Pantry
from ..models.substance import Substance
from ..schemas.substance_schema import SubstanceSchema

parser = reqparse.RequestParser()
parser.add_argument('nature')

substance_schema = SubstanceSchema()
substances_schema = SubstanceSchema(many=True)


class SubstanceResource(Resource):
    def get(self):
        args = parser.parse_args()
        nature = args['nature']
        pantry = Pantry()

        substances = pantry.find_substances_by_nature(nature)

        return substances_schema.dump(substances)

    def post(self):
        args = parser.parse_args()
        nature = args['nature']

        pantry = Pantry()

        substance = Substance(nature=nature)

        pantry.add_substance(substance)

        return substance_schema.dump(substance)


def init_app(app, api):
    api.add_resource(SubstanceResource, '/substance')
