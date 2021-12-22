try:
    import django
except ImportError:
    pass
else:
    if django.VERSION < (3, 2):
        default_app_config = "webpack_boilerplate.apps.WebpackBoilerplateConfig"
