from injector import Injector
from quart.views import MethodViewType

class ViewInjectorMeta(MethodViewType):
    def get_injector(self):
        return self.get_app().extensions['injector']

    def __call__(cls, *args, **kwargs):
        return cls.get_injector().create_object(
            cls.__bases__[0],
            additional_kwargs=kwargs
        )

def init_app(app, modules):
    modules.append(configure_injector)

    injctr = Injector()
    for module in modules:
        injctr.binder.install(module)
    app.extensions['injector'] = injctr

def configure_injector(binder):
    """
    Add any general purpose injectables, not included in a submodule
    """
    pass
