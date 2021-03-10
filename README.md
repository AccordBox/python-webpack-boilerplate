# README

## Goal

This project is to provide Webpack solution to your Django & Flask projects.

You can check [this blog](https://www.accordbox.com/blog/new-webpack-boilerplate-project-django-flask/) to learn more why it is created.

## What is included.

1. A `Webpack project template` which has good structure, easy to use and customize. User can create frontend project using `cookiecutter`, and use it even they have no idea how to config Webpack.
1. Template tags which can help load Webpack bundle file in the templates, it is smart to `auto load` dependency files.

## Features

- **Supports Django and Flask** (will support more framework in the future)
- Automatic multiple entry points
- Automatic code splitting
- Hot Module Replacement (HMR)
- Easy to config and customize
- ES6 Support via [babel](https://babeljs.io/) (v7)
- JavaScript Linting via [eslint-loader](https://github.com/MoOx/eslint-loader)
- SCSS Support via [sass-loader](https://github.com/jtangelder/sass-loader)
- Autoprefixing of browserspecific CSS rules via [postcss](https://postcss.org/) and [autoprefixer](https://github.com/postcss/autoprefixer)
- Style Linting via [stylelint](https://stylelint.io/)

## Optional support

*Need install extra packages*

- React
- Vue

## Documentation

1. [Setup With Django](https://python-webpack-boilerplate.readthedocs.io/en/latest/setup_with_django/)
1. [Setup With Flask](https://python-webpack-boilerplate.readthedocs.io/en/latest/setup_with_flask/)
1. [Frontend Workflow](https://python-webpack-boilerplate.readthedocs.io/en/latest/frontend/)
1. [Import React](https://python-webpack-boilerplate.readthedocs.io/en/latest/react/)
1. [Import Vue](https://python-webpack-boilerplate.readthedocs.io/en/latest/vue/)

## Special Thanks

* [django-webpack-loader](https://github.com/owais/django-webpack-loader)
* [rails/webpacker](https://github.com/rails/webpacker)
* [wbkd/webpack-starter](https://github.com/wbkd/webpack-starter)
