# Setup With Flask

## Install Package

```bash
$ pip install Flask
$ mkdir example
$ cd example
```

Next, install package

```bash
$ pip install python-webpack-boilerplate
```

Create `app.py`

```python
import os
from flask import Flask

app = Flask(__name__)

@app.cli.command("webpack_init")
def webpack_init():
    from cookiecutter.main import cookiecutter
    import webpack_boilerplate
    pkg_path = os.path.dirname(webpack_boilerplate.__file__)
    cookiecutter(pkg_path, directory="frontend_template")
```

Here we created a `webpack_init` custom command to help us create `frontend` project.

```bash
$ env FLASK_APP=app.py flask webpack_init

project_slug [frontend]:
run_npm_command_at_root [y]:
[SUCCESS]: Frontend app 'frontend' has been created.
```

Now a new `frontend` directory is created which contains pre-defined files for our frontend project.

```bash
├── frontend
│   ├── src
│   ├── vendors
│   └── webpack
├── manage.py
├── package-lock.json
├── package.json
├── postcss.config.js
└── requirements.txt
```

## Frontend

!!! note
    If you have no nodejs installed, please install it first by using below links

    1. On [nodejs homepage](https://nodejs.org/en/download/)
    1. Using [nvm](https://github.com/nvm-sh/nvm) I recommend this way.

```bash
$ node -v
v20.9.0
$ npm -v
10.1.0
```

Now go to directory which contains `package.json`, by default, it is root directory.

```bash
# install dependency packages
$ npm install

# run webpack in watch mode
$ npm run watch
```

!!! note
    run watch means webpack will watch source files and recompile whenever they change

The build files now can be found in `frontend/build` directory

```
build
├── css
├── js
├── manifest.json
└── vendors
```

!!! note
    You can check [Frontend Workflow](frontend.md) to learn more about frontend stuff

## Config Flask

Update `app.py`

```python
import os
from pathlib import Path
from flask import Flask, render_template
from webpack_boilerplate.config import setup_jinja2_ext


BASE_DIR = Path(__file__).parent
app = Flask(__name__, static_folder="frontend/build", static_url_path="/static/")
app.config.update({
    'WEBPACK_LOADER': {
        'MANIFEST_FILE': BASE_DIR / "frontend/build/manifest.json",
    }
})
setup_jinja2_ext(app)


@app.cli.command("webpack_init")
def webpack_init():
    from cookiecutter.main import cookiecutter
    import webpack_boilerplate
    pkg_path = os.path.dirname(webpack_boilerplate.__file__)
    cookiecutter(pkg_path, directory="frontend_template")


@app.route("/")
def hello():
    return render_template('index.html')
```

1. We add the above `frontend/build` to `static_folder` so Flask can find the static assets (img, font and others)
1. `static_url_path` is set to `/static/`
1. We add `MANIFEST_FILE` location to the `WEBPACK_LOADER` so our custom loader can help us load JS and CSS.
1. Remember to run `setup_jinja2_ext(app)` so we can us custom template tag in Jinja2 

## Load the bundle files

Add `index.html` to `templates`

```
├── app.py
├── frontend
└── templates
    └── index.html
```

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Index</title>
  <script src="https://cdn.tailwindcss.com"></script>
  {{ stylesheet_pack('app') }}
  {{ javascript_pack('app', attrs='defer') }}
</head>
<body>

<div class="bg-gray-50 py-5" data-jumbotron>
  <div class="container mx-auto px-4 py-10">
    <h1 class="text-4xl font-bold leading-tight">Welcome to Our Website</h1>
    <p class="mt-4 text-lg">This is a hero section built using Tailwind CSS.</p>
    <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 mt-6 rounded-lg">Get Started</button>
    <div class="flex justify-center">
      <img src="{{ url_for('static', filename='vendors/images/webpack.png') }}"/>
    </div>
  </div>
</div>

</body>
</html>
```

!!! note
    1. Here we use `Tailwind CDN` to help user to do quick test, please remove it later.
    1. You can import multiple entry files using one `javascript_pack` statement
    1. The `javascript_pack` would also **import dependency files automatically to handle code splitting**
    1. You can use `attrs` to set custom attributes

## Manual Test

```bash
$ env FLASK_APP=app.py flask run
```

Now check on [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and you should be able to see a welcome page.

The source code can also be found in the [Examples](https://github.com/AccordBox/python-webpack-boilerplate/tree/master/examples/)
