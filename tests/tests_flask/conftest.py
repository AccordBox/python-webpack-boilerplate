import pytest


@pytest.fixture
def app():
    from examples.flask_basic.app import app

    return app
