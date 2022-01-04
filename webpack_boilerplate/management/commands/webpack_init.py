import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from cookiecutter.main import cookiecutter

        pkg_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        cookiecutter(pkg_path, directory="frontend_template")
