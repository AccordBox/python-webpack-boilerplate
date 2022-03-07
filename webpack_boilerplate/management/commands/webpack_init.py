import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--no-input", action="store_true", help="Do not ask for input.",
        )

    def handle(self, *args, **options):
        from cookiecutter.main import cookiecutter

        pkg_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        if options["no_input"]:
            cookiecutter(pkg_path, directory="frontend_template", no_input=True)
        else:
            cookiecutter(pkg_path, directory="frontend_template")
