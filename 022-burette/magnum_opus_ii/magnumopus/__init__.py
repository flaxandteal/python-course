from quart_openapi import Pint

def create_app():
    from . import models, resources, schemas, logger, repositories, injection

    app = Pint(__name__, title='Magnum Opus')

    # This could be used to separate by environment
    app.config.from_object('magnumopus.config.Config')

    # This helps avoid cyclic dependencies
    modules = []

    modules += logger.init_app(app)
    modules += models.init_app(app)
    modules += resources.init_app(app)
    modules += repositories.init_app(app)
    modules += schemas.init_app(app)

    injection.init_app(app, modules)

    return app
