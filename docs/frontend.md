# Frontend

## Why Webpack

!!! note
    webpack is an open-source JavaScript module bundler. It is made primarily for JavaScript, but it can transform front-end assets such as HTML, CSS, and images if the corresponding loaders are included

1. `Webpack` is the most popular bundle solution in the frontend community today, it has received 50k stars on Github.
1. It has a great ecosystem, many plugins, loaders. If we search `webpack` on npmjs.com, we can get 20k resulst.
1. If we do not need `React`, `Vue`, we can still use Webpack to help us compile `ES6`, `SCSS` and do many other things (Many people do not know that!)
1. With a proper config, Webpack can save time and let us build modern web application in quick way.

## Structures

After creating frontend project from the template, you will have file structures like this.

```
frontend
├── package.json
├── src
│   ├── application
│   ├── components
│   └── styles
├── vendors
│   └── images
│       ├── sample.jpg
│       └── webpack.png
```

1. Components can be placed at `src/components`
1. SCSS and CSS code can be put at `src/styles`
1. Static assets such as images, fonts and other files can be put at `vendors`

## Compile

!!! note
    If you have no nodejs installed, please install it first by using below links

    1. On [nodejs homepage](https://nodejs.org/en/download/)
    1. Using [nvm](https://github.com/nvm-sh/nvm) I recommend this way.

```bash
# install dependency packages
$ npm install
# run webpack in watch mode
$ npm run watch
```

You will see `build` directory is created under `frontend` directory

1. `manifest.json` contains assets manifest info.
1. We can get the dependency of the entrypoint through `manifest.json`
1. So in templates, we can only import entrypoint without dependency files.

For example, `{{ javascript_pack('app', attrs='charset="UTF-8"') }}` would generate HTMl like this

```html
<script type="text/javascript" src="/static/js/runtime.js" charset="UTF-8"></script>
<script type="text/javascript" src="/static/js/vendors-node_modules_bootstrap_dist_js_bootstrap_bundle_js.js" charset="UTF-8"></script>
<script type="text/javascript" src="/static/js/app.js" charset="UTF-8"></script>
```

1. `app` is entrypoint file
1. `/static/js/runtime.js` and `/static/js/vendors-node_modules_bootstrap_dist_js_bootstrap_bundle_js.js` are all dependency files.
1. `javascript_pack` helps us import bundle files transparently

## NPM commands

There are three npm commands for us to use

### npm run watch

`npm run watch` would run webpack in `watch` mode.

webpack can watch files and recompile whenever they change

### npm run start

`npm run start` will launch a server process, which makes `live reloading` possible.

If you change JS or SCSS files, the web page would auto refresh after the change. Now the server is working on port 9091 by default, but you can change it in `webpack/webpack.config.dev.js`

### npm run build

[production mode](https://webpack.js.org/guides/production/), Webpack would focus on minified bundles, lighter weight source maps, and optimized assets to improve load time.

### What should I use

1. If you are developing, use `npm run watch` or `npm run start`
1. You should use `npm run build` in deployment

## Deployment Notes

[Deployment Notes](deployment.md)
