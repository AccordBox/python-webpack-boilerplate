# Live Reload

With `webpack-dev-server`, we can use it to auto reload web page when the code of the project changed.

Please edit `frontend/webpack/webpack.config.dev.js`

```js
devServer: {
  host: "0.0.0.0",
  port: 9091,
  headers: {
    "Access-Control-Allow-Origin": "*",
  },
  devMiddleware: {
    writeToDisk: true,
  },
  watchFiles: [
    Path.join(__dirname, '../../django_app/**/*.py'),
    Path.join(__dirname, '../../django_app/**/*.html'),
  ],
},
```

Notes:

1. Add `watchFiles` to the `devServer` object.
1. Here we tell `webpack-dev-server` to watch all `.py` and `.html` files under the `django_app` directory.

Run Webpack dev server with `npm run start`

Now if we change code in the editor, the web page will live reload, which is awesome!
