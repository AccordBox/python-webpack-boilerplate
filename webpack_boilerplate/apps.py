try:
    from django.apps import AppConfig
except ImportError:
    from types import NoneType

    AppConfig = NoneType


class WebpackBoilerplateConfig(AppConfig):
    name = "webpack_boilerplate"
    verbose_name = "Webpack Boilerplate"
