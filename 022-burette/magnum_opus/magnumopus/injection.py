from flask_injector import FlaskInjector

def init_app(app, modules):
    modules.append(configure_injector)
    FlaskInjector(app=app, modules=modules)

def configure_injector(binder):
    """
    Add any general purpose injectables, not included in a submodule
    """
    pass
