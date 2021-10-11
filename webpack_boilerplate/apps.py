try:
    from django.apps import AppConfig
except ImportError:
    from types import NoneType

    AppConfig = NoneType


class WebpackLoaderConfig(AppConfig):
    name = "webpack_loader"
    verbose_name = "Webpack Loader"
