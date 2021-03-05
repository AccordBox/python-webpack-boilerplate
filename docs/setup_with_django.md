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

Add 'webpack_loader' to the `INSTALLED_APPS` in `example/settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'webpack_loader',
]
```

Let's run Django command to create frontend project from the templates

```bash
$ python manage.py webpack_init
# here we use the default frontend slug
project_slug [frontend]:
```

Now a new `frontend` directory is created which contains pre-defined files for our frontend project.

```
frontend
├── README.md
├── package-lock.json
├── package.json
├── postcss.config.js
├── src
├── vendors
└── webpack
```

## Frontend

> If you have no nodejs installed, please install it first by using below links

1. On [nodejs homepage](https://nodejs.org/en/download/)
1. Using [nvm](https://github.com/nvm-sh/nvm) I recommend this way.

```bash
$ node -v
v12.20.0
$ npm -v
6.14.8
```

Now go to `frontend`

```python
# install dependency packages
$ npm install
# run webpack in watch mode
$ npm run watch
```

> run watch means webpack will watch source files and recompile whenever they change

The build files now can be found in `frontend/build` directory

```
build
├── css
├── js
├── manifest.json
└── vendors
```

## Config Django

Add code below to Django settings `example/settings.py`

```python
import os

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend/build"),
]

WEBPACK_LOADER = {
    'MANIFEST_FILE': os.path.join(BASE_DIR, "frontend/build/manifest.json"),
}
```

1. We add the above `frontend/build` to `STATICFILES_DIRS` so Django can find the static assets (img, font and others)
1. We add `MANIFEST_FILE` location to the `WEBPACK_LOADER` so our custom loader can help us load JS and CSS.

## Load the bundle files

Let's do a quick test on the home page.

Update `example/urls.py`

```python
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),     # this is new
    path('admin/', admin.site.urls),
]
```

```bash
$ mkdir example/templates

├── frontend
├── manage.py
└── example
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── templates             # this is new
    ├── urls.py
    └── wsgi.py
```

Update `TEMPLATES` in `example/settings.py`, so Django can know where to find the templates

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['example/templates'],                      # this is new
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

```django
{% load webpack_loader static %}

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Index</title>
  {% stylesheet_pack 'app' %}
</head>
<body>

<div class="jumbotron py-5">
  <div class="container">
    <h1 class="display-3">Hello, world!</h1>
    <p>This is a template for a simple marketing or informational website. It includes a large callout called a
      jumbotron and three supporting pieces of content. Use it as a starting point to create something more unique.</p>
    <p><a class="btn btn-primary btn-lg" href="#" role="button">Learn more »</a></p>

    <div class="d-flex justify-content-center">
      <img src="{% static 'vendors/images/webpack.png' %}" class="img-fluid"/>
    </div>

  </div>
</div>

{% javascript_pack 'app' 'app2' attrs='charset="UTF-8"' %}

</body>
</html>
```

1. We `load webpack_loader` at the top of the template
1. We can still use `static` to import image from the frontend project.
1. We use `stylesheet_pack` and `javascript_pack` to load CSS and JS bundle files to Django

## Manual Test

```bash
$ python manage.py migrate
$ python manage.py runserver
```

Now check on [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and you should be able to see a welcome page.

The source code can also be found in the [Examples](https://github.com/AccordBox/python-webpack-boilerplate/tree/master/examples/)
