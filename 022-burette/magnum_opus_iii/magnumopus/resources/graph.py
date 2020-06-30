from quart import request, jsonify
from quart_openapi import Resource
from injector import inject
from typing import Dict
from ariadne import graphql
from ariadne.constants import PLAYGROUND_HTML
from graphql.type import GraphQLSchema
from ..injection import ViewInjectorMeta
from ..repositories.pantry import Pantry
from ..models import db

class GraphResource(Resource):
    @inject
    def __init__(self, schema: GraphQLSchema):
        super(GraphResource, self).__init__()

        self._schema = schema

    async def get(self):
        return (PLAYGROUND_HTML, 200)

    async def post(self):
        data = await request.get_json()
        success, result = await graphql(
            self._schema,
            data,
            context_value=request
        )

        return jsonify(result), (200 if success else 400)


def init_app(app):
    class AppGraphResource(GraphResource, metaclass=ViewInjectorMeta):
        get_app = lambda: app

    app.route('/graphql', endpoint='graphql')(AppGraphResource)

    return []
