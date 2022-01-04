# Introduction

## Usage

After [creating frontend project from the template](frontend), you will have file structures like this.

``` hl_lines="4 8 10 12"
frontend
├── package.json
├── src
│   ├── application
│   │   # webpack entry files here
│   │   ├── app.js
│   │   └── app2.js
│   ├── components
│   │   └── sidebar.js
│   └── styles
│       └── index.scss
├── vendors
│   └── images
│       ├── sample.jpg
│       └── webpack.png
```

1. You can create entry file in `src/application` (This project would detect the entry files automatically so you do not need to config Webpack)
1. Reusable components can be placed at `src/components`
1. SCSS and CSS code can be put at `src/styles`
1. Static assets such as images, fonts and other files can be put at `vendors`

```bash
$ cd frontend

# install dependency packages
$ npm install
# build js, scss files
$ npm run start
```

Now you can load bundle file in templates like

```html
{% stylesheet_pack 'app' %}
{% javascript_pack 'app' 'app2' attrs='charset="UTF-8"' %}
```

!!! note
    1. You can import multiple entry files using one `javascript_pack` statement
    1. The `javascript_pack` would also **import dependency files automatically to handle code splitting**
    1. You can use `attrs` to set custom attributes
