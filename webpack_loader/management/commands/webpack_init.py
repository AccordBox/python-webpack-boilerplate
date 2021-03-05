from pathlib import Path

from cookiecutter.main import cookiecutter
from django.core.management.base import BaseCommand
from webpack_loader import PKG_BASE_DIR


class Command(BaseCommand):
    def handle(self, *args, **options):
        cookiecutter(str(PKG_BASE_DIR / "frontend_template"))
