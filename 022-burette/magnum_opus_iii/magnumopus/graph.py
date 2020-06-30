from quart import request, jsonify
from graphql import GraphQLSchema
from ariadne import ObjectType, make_executable_schema, graphql
from .schemas import init_graph as init_graph_schemas
from .resources import init_graph as init_graph_resources

TYPE_DEFS = """
    type Query {
        substances(nature: String!): [Substance]
    }
"""

class InjectorObjectType(ObjectType):
    def __init__(self, *args, app=None, **kwargs):
        super(InjectorObjectType, self).__init__(*args, **kwargs)
        self._app = app

    def get_injector(self):
        return self._app.extensions['injector']

    def field(self, name: str):
        g = super(InjectorObjectType, self).field(name)
        def injected_resolver(f):
            def _inject_resolver(*args, **kwargs):
                self._app.logger.error(name)
                inj = self.get_injector()
                return inj.call_with_injection(
                    f, args=args, kwargs=kwargs
                )
            return g(_inject_resolver)
        return injected_resolver

def init_app(app):
    query = InjectorObjectType('Query', app=app)

    type_defs = [TYPE_DEFS] + init_graph_schemas(query)
    resolvers = [query] + init_graph_resources(query)

    schema = make_executable_schema(type_defs, resolvers)

    return [
        lambda binder: binder.bind(
            GraphQLSchema,
            to=schema
        )
    ]
