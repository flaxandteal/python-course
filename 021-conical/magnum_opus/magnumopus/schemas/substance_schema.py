from marshmallow import fields

from . import ma

from ..services.assessor import assess_whether_substance_is_philosophers_stone

class SubstanceSchema(ma.Schema):
    is_philosophers_stone = fields.Function(
        assess_whether_substance_is_philosophers_stone
    )

    class Meta:
        fields = ("nature", "is_philosophers_stone")
