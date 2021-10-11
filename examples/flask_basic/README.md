# Flask Example

## How to run

```bash
# install python-webpack-boilerplate
$ python -m pip install git+https://github.com/AccordBox/python-webpack-boilerplate

# install Flask
$ pip install -r requirements.txt

# go to frontend directory (whic is soft link in Github repo)

# install frontend dependency
$ npm install

# run webpack with watch mode
$ npm run watch

# launch Flask server in another terminal
$ env FLASK_APP=app.py flask run
```

Now you can check on [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Files you need to check

1. `templates/index.html`
1. `app.py`
1. `frontend/src/`