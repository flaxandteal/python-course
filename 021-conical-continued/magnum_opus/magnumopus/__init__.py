from flask import Flask

def create_app():
    from . import models, resources, schemas, logger

    app = Flask(__name__)

    # This helps avoid cyclic dependencies
    logger.init_app(app)
    models.init_app(app)
    resources.init_app(app)
    schemas.init_app(app)

    return app
