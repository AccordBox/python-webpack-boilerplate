import re

__all__ = ("load_config", "get_setting_value")


def load_from_django():
    from django.conf import settings

    DEFAULT_CONFIG = {
        "CACHE": not settings.DEBUG,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
        "LOADER_CLASS": "webpack_boilerplate.loader.WebpackLoader",
    }

    user_config = dict(DEFAULT_CONFIG, **getattr(settings, "WEBPACK_LOADER", {}))

    user_config["ignores"] = [re.compile(I) for I in user_config["IGNORE"]]
    user_config["web_framework"] = "django"
    return user_config


def load_from_flask():
    from flask import current_app

    DEFAULT_CONFIG = {
        "CACHE": not current_app.config["DEBUG"],
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
        "LOADER_CLASS": "webpack_boilerplate.loader.WebpackLoader",
    }

    user_config = dict(DEFAULT_CONFIG, **current_app.config["WEBPACK_LOADER"])

    user_config["ignores"] = [re.compile(I) for I in user_config["IGNORE"]]
    user_config["web_framework"] = "flask"
    return user_config


def load_config(name):
    try:
        import django

        return load_from_django()
    except ImportError:
        pass

    try:
        import flask

        return load_from_flask()
    except ImportError:
        pass

    raise Exception("can not load config from this project")


def get_setting_value(key):
    try:
        import django
        from django.conf import settings

        return settings.get(key, None)
    except ImportError:
        pass

    try:
        import flask
        from flask import current_app

        map = {"STATIC_URL": "STATIC_URL"}
        return current_app.config.get(map[key], None)
    except ImportError:
        pass


def setup_jinja2_ext(app):
    """
    Run by flask app
    """
    from .contrib.jinja2ext import WebpackExtension

    app.jinja_env.add_extension(WebpackExtension)
