from flask import Flask

def create_app():
    from . import models, resources, schemas, logger

    app = Flask(__name__)

    # This could be used to separate by environment
    app.config.from_object('magnumopus.config.Config')

    # This helps avoid cyclic dependencies
    logger.init_app(app)
    models.init_app(app)
    resources.init_app(app)
    schemas.init_app(app)

    return app
