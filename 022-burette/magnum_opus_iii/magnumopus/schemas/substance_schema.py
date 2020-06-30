from marshmallow import fields

from . import ma

from ..models.substance import Substance
from ..services.assessor import assess_whether_substance_is_philosophers_stone

SUBSTANCE_GRAPH_SCHEMA = """
    type Substance {
        nature: String!,
        state: [String]!
    }
"""

class SubstanceSchema(ma.SQLAlchemySchema):
    is_philosophers_stone = fields.Function(
        assess_whether_substance_is_philosophers_stone
    )

    class Meta:
        model = Substance
        fields = ('id', 'nature', 'is_philosophers_stone', 'state')

    id = fields.Integer()
    nature = fields.String()
    state = fields.Function(lambda model: model.state or [])

def init_graph(query):
    return SUBSTANCE_GRAPH_SCHEMA
