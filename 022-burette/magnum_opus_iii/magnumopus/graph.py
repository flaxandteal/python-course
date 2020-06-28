from quart import request, jsonify
from ariadne import ObjectType, make_executable_schema, graphql
from ariadne.constants import PLAYGROUND_HTML

from .repositories import PANTRY_STORES

PANTRY = PANTRY_STORES['list']

type_defs = """
    type Query {
        substances(nature: String!): [Substance]
    }

    type Substance {
        nature: String!,
        state: [String]!
    }
"""

query = ObjectType('Query')
substance = ObjectType('Substance')

@query.field('substances')
def resolve_substances(obj, *_, nature='Unknown'):
    return PANTRY.find_substances_by_nature(nature)


@substance.field('nature')
def resolve_nature(obj, *_):
    return obj.nature

@substance.field('state')
def resolve_state(obj, *_):
    return obj.state

schema = make_executable_schema(type_defs, query, substance)

async def graphql_server():
    data = await request.get_json()
    success, result = await graphql(
        schema,
        data,
        context_value=request
    )

    return jsonify(result), (200 if success else 400)

def init_app(app):
    app.route('/graphql', methods=['GET'], endpoint='graphql_playground')(
        lambda: (PLAYGROUND_HTML, 200)
    )

    app.route('/graphql', methods=['POST'], endpoint='graphql_server')(
        graphql_server
    )

    return []
