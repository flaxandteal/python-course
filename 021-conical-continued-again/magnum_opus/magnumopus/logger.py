import logging

def init_app(app):
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)
