from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from cookiecutter.main import cookiecutter
        from webpack_loader import GIT_URL

        cookiecutter(GIT_URL, directory="frontend_template")
