# NPM commands

There are three npm commands for us to use

## Watch

`npm run watch` would run webpack in `watch` mode.

!!! Watch Mode
    webpack can watch files and recompile whenever they change

## Dev Server

`npm run start` will launch a server process, which makes `live reloading` possible.

!!! Live reloading
    If you change JS or SCSS files, the web page would auto refresh after the change. Now the server is working on port 9091 by default, but you can change it in `webpack.dev.js`

## Production build

`npm run build`

!!! production mode
    [production mode](https://webpack.js.org/guides/production/), Webpack would focus on minified bundles, lighter weight source maps, and optimized assets to improve load time.

## What should I use

1. If you are developing, use `npm run watch` or `npm run start`
1. You should use `npm run build` in deployment