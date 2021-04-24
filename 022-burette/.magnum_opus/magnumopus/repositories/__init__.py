from .pantry import Pantry
from .list_pantry import ListPantry
from .sqlalchemy_pantry import SQLAlchemyPantry
from .cqlalchemy_pantry import CQLAlchemyPantry

PANTRY_STORES = {
    'sqlalchemy': SQLAlchemyPantry,
    'cqlalchemy': CQLAlchemyPantry,
    'list': ListPantry()      # we instantiate this, as we want a singleton cupboard
}

def init_app(app):
    return [lambda binder: configure_injector(binder, app)]

def configure_injector(binder, app):
    pantry_cls = PANTRY_STORES[app.config['PANTRY_STORE']]

    binder.bind(
        Pantry, to=pantry_cls
    )
