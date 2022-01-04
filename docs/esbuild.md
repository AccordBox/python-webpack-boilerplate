# esbuild

By default, this project use `Babel` to transpile JS code.

For better performance, we can switch to `esbuild`

## Something you should know

From `ESbuld` doc [https://esbuild.github.io/content-types/#es5](https://esbuild.github.io/content-types/#es5)

> Transforming ES6+ syntax to ES5 is not supported yet. However, if you're using esbuild to transform ES5 code, you should still set the target to es5. This prevents esbuild from introducing ES6 syntax into your ES5 code.

So if your project still need to support some old browser, `Babel` is still better option for you.

## Install

```bash
$ cd frontend
$ npm install -D esbuild-loader
```

Next, let's change Webpack config to use `esbuild-loader` to process our JS files

Edit *webpack.config.dev.js* and *webpack.config.watch.js*

```js
{
  test: /\.js$/,
  include: Path.resolve(__dirname, "../src"),
  loader: "esbuild-loader",             // replace loader for the js files
  options: {                            // we can pass options as we like
    target: ['es2015']
  }
},
```

Edit *webpack.config.prod.js*

```js
{
  test: /\.js$/,
  include: Path.resolve(__dirname, "../src"),
  loader: "esbuild-loader",
  options: {                            // we can pass options as we like
    target: ['es2015']
  }
},
```

That is it, now you can run `npm run start` or `npm run build` to compile frontend assets.

## Reference

1. [https://github.com/privatenumber/esbuild-loader](https://github.com/privatenumber/esbuild-loader)
1. [https://esbuild.github.io/](https://esbuild.github.io/)
