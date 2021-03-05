import os
from pathlib import Path
from flask import Flask, render_template
from webpack_loader.config import setup_jinja2_ext


BASE_DIR = Path(__file__).parent
app = Flask(__name__, static_folder="frontend/build", static_url_path="/static/")
app.config.update({
    'WEBPACK_LOADER': {
        'MANIFEST_FILE': os.path.join(BASE_DIR, "frontend/build/manifest.json"),
    }
})
setup_jinja2_ext(app)


@app.cli.command("webpack_init")
def webpack_init():
    from cookiecutter.main import cookiecutter
    from webpack_loader import GIT_URL
    cookiecutter(GIT_URL, directory='frontend_template')


@app.route("/")
def hello():
    return render_template('index.html')
