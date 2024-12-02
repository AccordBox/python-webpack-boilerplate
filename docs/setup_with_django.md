# Setup With Django

## Install Package

```bash
$ pip install Django
$ django-admin startproject example
$ cd example
```

Now your Django projects would seem like this:

```
├── manage.py
└── example
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

Next, install package

```bash
$ pip install python-webpack-boilerplate
```

Add `webpack_boilerplate` to the `INSTALLED_APPS` in `example/settings.py`

```python hl_lines="9"
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'webpack_boilerplate',
]
```

Let's run Django command to create frontend project from the templates

```bash hl_lines="3 4"
$ python manage.py webpack_init

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
v20.10.0
$ npm -v
10.2.3
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
    You can check [Frontend Workflow](frontend.md) to learn more details about the frontend workflow

After Webpack has compiled the assets, we can load the assets in Django.

## Config Django

Add code below to Django settings `example/settings.py`

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend/build"),
]

WEBPACK_LOADER = {
    'MANIFEST_FILE': os.path.join(BASE_DIR, "frontend/build/manifest.json"),
}
```

1. We add the above `frontend/build` to `STATICFILES_DIRS` so Django can find the static assets (img, font and others)
1. We add `MANIFEST_FILE` location to the `WEBPACK_LOADER` so our `webpack_loader` can know where to find the manifest file.

## Load the bundle files

Let's do a quick test on the home page.

Update `example/urls.py`

```python hl_lines="6"
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),     # new
    path('admin/', admin.site.urls),
]
```

```bash hl_lines="9"
$ mkdir example/templates

├── frontend
├── manage.py
└── example
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── templates
    ├── urls.py
    └── wsgi.py
```

Update `TEMPLATES` in `example/settings.py`, so Django can know where to find the templates

```python hl_lines="4"
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['example/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Add `index.html` to the above `example/templates`

```html hl_lines="1 9 10 20"
{% load webpack_loader static %}

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Index</title>
  <script src="https://cdn.tailwindcss.com"></script>
  {% stylesheet_pack 'app' %}
  {% javascript_pack 'app' attrs='defer' %}
</head>
<body>

<div class="bg-gray-50 py-5" data-jumbotron>
  <div class="container mx-auto px-4 py-10">
    <h1 class="text-4xl font-bold leading-tight">Welcome to Our Website</h1>
    <p class="mt-4 text-lg">This is a hero section built using Tailwind CSS.</p>
    <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 mt-6 rounded-lg">Get Started</button>
    <div class="flex justify-center">
      <img src="{% static 'vendors/images/webpack.png' %}"/>
    </div>
  </div>
</div>

</body>
</html>
```

1. Here we use `Tailwind CDN` to help user to do quick test, please remove it later.
2. We `load webpack_loader` at the top of the template
3. We can still use `static` tag to import image from the frontend project.
4. We use `stylesheet_pack` and `javascript_pack` to load CSS and JS bundle files to Django

!!! note
    1. When your javascript and css files grow bigger and bigger, code splitting would be done automatically by Webpack.
    1. The `javascript_pack` would **import dependency files automatically to handle code splitting**
    1. You can import **multiple entry files** using `stylesheet_pack` and `javascript_pack` (`{% javascript_pack 'app' 'vendors'`) if you prefer manual code splitting.

## Manual Test

```bash
$ python manage.py migrate
$ python manage.py runserver
```

Now check on [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and you should be able to see a welcome page.

In the devtools console, you should see

```bash
dom ready
jumbotron.js:8 Jumbotron initialized for node: [object HTMLDivElement]
```

The source code can also be found in the [Examples](https://github.com/AccordBox/python-webpack-boilerplate/tree/master/examples/)

## Live Reload

[Live Reload Support](live_reload.md)
