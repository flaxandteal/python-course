from . import substance
from . import alembic_instruction
from . import graph

def init_app(app):
    substance.init_app(app)
    alembic_instruction.init_app(app)
    graph.init_app(app)
    return []

def init_graph(graph):
    resolvers = []
    resolvers += substance.init_graph(graph)
    return resolvers
