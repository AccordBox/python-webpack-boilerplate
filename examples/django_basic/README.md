# Django Example

## How to run

```bash
# install python-webpack-boilerplate
$ python -m pip install git+https://github.com/AccordBox/python-webpack-boilerplate

# install Django
$ pip install -r requirements.txt

# go to frontend directory (whic is soft link in Github repo)

# install frontend dependency
$ npm install

# run webpack with watch mode
$ npm run watch

# launch Django server in another terminal
$ ./manage.py migrate
$ ./manage.py runserver
```

Now you can check on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Files you need to check

1. `example/templates/index.html`
1. `example/settings.py`
1. `frontend/src/`
