from marshmallow import fields

from . import ma

from ..models.substance import Substance
from ..services.assessor import assess_whether_substance_is_philosophers_stone

class SubstanceSchema(ma.SQLAlchemySchema):
    is_philosophers_stone = fields.Function(
        assess_whether_substance_is_philosophers_stone
    )

    class Meta:
        model = Substance
        fields = ('id', 'nature', 'is_philosophers_stone', 'state')

    id = ma.auto_field()
    nature = ma.auto_field()
