import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from cookiecutter.main import cookiecutter

        pkg_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        app_path = cookiecutter(pkg_path, directory="frontend_template")

        app_name = os.path.basename(app_path)

        self.stdout.write(
            self.style.SUCCESS(
                f"Frontend app '{app_name}' "
                f"has been successfully created. "
                f"To know more, check https://python-webpack-boilerplate.rtfd.io/en/latest/frontend/"
            )
        )
