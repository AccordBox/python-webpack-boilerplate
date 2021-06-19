# README

[![Build Status](https://github.com/AccordBox/python-webpack-boilerplate/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/AccordBox/python-webpack-boilerplate/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/python-webpack-boilerplate.svg)](https://badge.fury.io/py/python-webpack-boilerplate)
[![Documentation](https://img.shields.io/badge/Documentation-link-green.svg)](https://python-webpack-boilerplate.rtfd.io/)

## Goal

**Jump start frontend project bundled by Webpack with Django, Flask quickly**

## What is included.

1. A `frontend project template` which has good structure, easy to use and customize. You can create the frontend project with just **ONE** command, and use it even you have no idea how to config Webpack.
1. Custom template tags which can help load Webpack bundle file in the templates transparently.

## Features

- **Supports Django and Flask** (will support more framework in the future)
- Automatic multiple entry points
- Automatic code splitting
- Hot Module Replacement (HMR) (auto reload web page if you edit JS or SCSS)
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
