from quart import request
from quart_openapi import Resource
from injector import inject
from typing import Dict
from ..injection import ViewInjectorMeta
from ..repositories.pantry import Pantry
from ..models import db
from ..models.substance import Substance
from ..schemas.substance_schema import SubstanceSchema

class SubstanceResource(Resource):
    @inject
    def __init__(self, pantry: Pantry, substance_schemas: Dict[str, SubstanceSchema]):
        super(SubstanceResource, self).__init__()

        self._pantry = pantry
        self._substance_schema = substance_schemas['one']
        self._substances_schema = substance_schemas['many']

    async def get(self):
        nature = request.args.get('nature')

        substances = self._pantry.find_substances_by_nature(nature)

        return {
            'result': self._substances_schema.dump(substances)
        }

    async def post(self):
        args = await request.get_json()

        nature = args['nature']

        pantry = self._pantry

        substance = Substance(nature=nature)

        pantry.add_substance(substance)

        pantry.commit()

        return self._substance_schema.dump(substance), 201


def init_app(app):
    class AppSubstanceResource(SubstanceResource, metaclass=ViewInjectorMeta):
        get_app = lambda: app

    app.route('/substance', endpoint='SubstanceResource')(AppSubstanceResource)
