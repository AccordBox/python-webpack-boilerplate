# Jump start frontend project bundled by Webpack

[![Build Status](https://github.com/AccordBox/python-webpack-boilerplate/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/AccordBox/python-webpack-boilerplate/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/python-webpack-boilerplate.svg)](https://badge.fury.io/py/python-webpack-boilerplate)
[![Documentation](https://img.shields.io/badge/Documentation-link-green.svg)](https://python-webpack-boilerplate.rtfd.io/)

## Difference between django-webpack-loader

When using `django-webpack-loader`, you need to create `Webpack` project on your own, which is not easy for many newbie Django developers.

`python-webpack-boilerplate` can let you play with modern frontend tech in Django, even you have no idea how to config Webpack.

## Features

- **Supports Django and Flask** (will support more framework in the future)
- Automatic multiple entry points
- Automatic code splitting
- Hot Module Replacement (HMR) (auto reload web page if you edit JS or SCSS)
- Easy to config and customize
- ES6 Support via [babel](https://babeljs.io/) (v7)
- JavaScript Linting via [eslint](https://eslint.org/)
- SCSS Support via [sass-loader](https://github.com/jtangelder/sass-loader)
- Autoprefixing of browserspecific CSS rules via [postcss](https://postcss.org/) and [postcss-preset-env](https://github.com/csstools/postcss-preset-env)
- Style Linting via [stylelint](https://stylelint.io/)

----

If you want to import **lightweight modern frontend solution** to your web app, or you do not like **heavy framework** such as React, Vue.

Please check my book [The Definitive Guide to Hotwire and Django](https://leanpub.com/hotwire-django)

----

## Documentation

1. [Setup With Django](https://python-webpack-boilerplate.readthedocs.io/en/latest/setup_with_django/)
2. [Setup With Flask](https://python-webpack-boilerplate.readthedocs.io/en/latest/setup_with_flask/)
3. [Frontend Workflow](https://python-webpack-boilerplate.readthedocs.io/en/latest/frontend/)

## Raising funds

If you like this project, please consider supporting my work. [Open Collective](https://opencollective.com/python-webpack-boilerplate)

---

<a href="https://opencollective.com/python-webpack-boilerplate#backers" target="_blank"><img src="https://opencollective.com/python-webpack-boilerplate/backers.svg?width=890"></a>

---

## Special Thanks

* [Definitive Guide to Django and Webpack](https://www.accordbox.com/blog/definitive-guide-django-and-webpack/)
* [django-webpack-loader](https://github.com/owais/django-webpack-loader)
* [rails/webpacker](https://github.com/rails/webpacker)
* [wbkd/webpack-starter](https://github.com/wbkd/webpack-starter)
