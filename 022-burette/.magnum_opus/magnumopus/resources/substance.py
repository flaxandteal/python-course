from flask_restful import Resource, reqparse
from injector import inject
from typing import Dict
from ..repositories.pantry import Pantry
from ..models import db
from ..models.substance import Substance
from ..schemas.substance_schema import SubstanceSchema

# parser = reqparse.RequestParser()
# parser.add_argument('nature')

# substance_schema = SubstanceSchema()
# substances_schema = SubstanceSchema(many=True)

# pantry_cls = SQLAlchemyPantry


class SubstanceResource(Resource):
    @inject
    def __init__(self, pantry: Pantry, substance_schemas: Dict[str, SubstanceSchema], parser_fcty=reqparse.RequestParser):
        super(SubstanceResource, self).__init__()

        self._pantry = pantry
        self._substance_schema = substance_schemas['one']
        self._substances_schema = substance_schemas['many']
        self._parser_fcty = parser_fcty

    def get(self):
        parser = self._parser_fcty()

        parser.add_argument('nature')

        args = parser.parse_args()

        nature = args['nature']

        substances = self._pantry.find_substances_by_nature(nature)

        return self._substances_schema.dump(substances)

    def post(self):
        parser = self._parser_fcty()

        parser.add_argument('nature')

        args = parser.parse_args()

        nature = args['nature']

        pantry = self._pantry

        substance = Substance(nature=nature)

        pantry.add_substance(substance)

        pantry.commit()

        return self._substance_schema.dump(substance), 201


def init_app(app, api):
    api.add_resource(SubstanceResource, '/substance')
