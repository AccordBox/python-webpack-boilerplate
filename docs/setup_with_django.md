# Setup With Django

We will show you how to integrate `python-webpack-boilerplate` with Django and use Tailwind v4 as the style solution.

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

```bash
$ python manage.py webpack_init
  [1/3] project_slug (frontend):
  [2/3] run_npm_command_at_root (y):
  [3/3] Select style_solution
    1 - tailwind
    2 - bootstrap
    3 - scss
    Choose from [1/2/3] (1): 1
 [SUCCESS]: Frontend app 'frontend' has been created. To know more, check https://python-webpack-boilerplate.rtfd.io/en/latest/frontend/
```

Here we use the default `Tailwind CSS` as our style solution.

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
v22.13.1
$ npm -v
10.9.2
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
    BASE_DIR / "frontend/build",
]

WEBPACK_LOADER = {
    'MANIFEST_FILE': BASE_DIR / "frontend/build/manifest.json",
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

```html
{% load webpack_loader static %}

<!DOCTYPE html>
<html>
<head>
  <title>Index</title>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% stylesheet_pack 'app' %}
</head>
<body>

<div class="jumbotron py-5">
  <div class="w-full max-w-7xl mx-auto px-4">
    <h1 class="text-4xl mb-4">Hello, world!</h1>
    <p class="mb-4">This is a template for a simple marketing or informational website. It includes a large callout called a
      jumbotron and three supporting pieces of content. Use it as a starting point to create something more unique.</p>

    <p><a class="btn-blue mb-4" href="#" role="button">Learn more »</a></p>

    <div class="flex justify-center">
      <img src="{% static 'vendors/images/webpack.png' %}"/>
    </div>
  </div>
</div>

{% javascript_pack 'app' %}

</body>
</html>
```

1. We `load webpack_loader` at the top of the template
2. We can still use `static` tag to import image from the frontend project.
3. We use `stylesheet_pack` and `javascript_pack` to load CSS and JS bundle files to Django

!!! note
    1. When your javascript and css files grow bigger and bigger, code splitting would be done automatically by Webpack.
    1. The `javascript_pack` would **import dependency files automatically to handle code splitting**
    1. You can import **multiple entry files** using `stylesheet_pack` and `javascript_pack` (`{% javascript_pack 'app' 'vendors'`) if you prefer manual code splitting.

## Manual Test

```bash
# restart webpack to let Tailwind auto scan
$ npm run watch

$ python manage.py migrate
$ python manage.py runserver
```

Now check on [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and you should be able to see a welcome page.

In the devtools console, you should see

```bash
dom ready
jumbotron.js:8 Jumbotron initialized for node: [object HTMLDivElement]
```

## Explicitly Specify Source Files

Even Tailwind 4 can AUTO scan all project files in the project directory, we still recommend to explicitly specify the source files to improve performance.

Below is an example of `frontend/src/styles/index.css`

```css
/*import tailwindcss and disable automatic source detection*/
@import "tailwindcss" source(none);

/*register frontend directory*/
@source "../";

/*register django templates*/
@source "../../../django_tailwind_app/**/*.html";

.jumbotron {
    /*should be relative path of the entry css file*/
    background-image: url("../../vendors/images/sample.jpg");
    background-size: cover;
}

@layer components{
    .btn-blue {
        @apply inline-flex items-center;
        @apply px-4 py-2;
        @apply font-semibold rounded-lg shadow-md;
        @apply text-white bg-blue-500;
        @apply hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400/50;
    }
}
```

## Live Reload

[Live Reload Support](live_reload.md)
