# Tailwind CSS

## Install Dependency

Go to `frontend` directory

```bash
$ npm install -D tailwindcss@latest postcss-import
```

Once done, update `postcss.config.js`

```
// https://tailwindcss.com/docs/using-with-preprocessors

module.exports = {
  plugins: [
    require('postcss-import'),
    require('tailwindcss/nesting')(require('postcss-nesting')),
    require('tailwindcss'),
    require('postcss-preset-env')({
      features: { 'nesting-rules': false }
    }),
  ]
};
```

Next, generate a config file for your project using the Tailwind CLI utility included when you install the `tailwindcss` npm package

```bash
$ npx tailwindcss init
```

Now `tailwind.config.js` is generated

```js
module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [],
}
```

## App.js

Remove Bootstrap bundle file from `src/application/app.js`

```js
// This is the scss entry file
import "../styles/index.scss";

// We can import other JS file as we like
import "../components/sidebar";

window.document.addEventListener("DOMContentLoaded", function () {
  window.console.log("dom ready 1");
});
```

Update *src/styles/index.scss*

```scss
@import "tailwindcss/base";
@import "tailwindcss/components";
@import "tailwindcss/utilities";

.jumbotron {
  // should be relative path of the entry scss file
  background-image: url("../../vendors/images/sample.jpg");
  background-size: cover;
}

.btn-blue {
  @apply inline-block py-4 px-4 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-75;
}
```

```
$ npm run start
```

Edit Django template `templates/index.html`

```html hl_lines="8 28"
{% load webpack_loader static %}

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Index</title>
  {% stylesheet_pack 'app' %}
</head>
<body>

<div class="jumbotron">
  <div class="w-full max-w-7xl p-4 mx-auto">
    <h1 class="text-4xl mb-4">Hello, world!</h1>

    <p class="mb-2">This is a template for a simple marketing or informational website. It includes a large callout called a
      jumbotron and three supporting pieces of content. Use it as a starting point to create something more unique.</p>

    <p class="mb-2"><a class="btn-blue" href="#" role="button">Learn more »</a></p>

    <div class="flex justify-center">
      <img src="{% static 'vendors/images/webpack.png' %}"/>
    </div>

  </div>
</div>

{% javascript_pack 'app' %}

</body>
</html>
```

```bash
$ python manage.py runserver
```

## Better performance

The default tailwindcss file size is a little big, let's improve it for better performance

Update `tailwind.config.js`

```js
const Path = require("path");

const pwd = process.env.PWD;
const purgePaths = [
  Path.join(pwd, "../example/templates/**/*.html"),
];
console.log(`tailwindcss purge by scanning ${purgePaths}`);

module.exports = {
  mode: 'jit',
  purge: purgePaths,
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
```

1. We set `purge` by passing `purgePaths`, here we passed `example` Django project template dir so tailwind will scan the templates to know which classes are used. Unused css will be removed from final bundle file.
1. **You might need to edit the `purgePaths` to include other Django app templates or JS file**   
1. We `Enabling JIT mode` by using `mode: 'jit'`

## Plugins

Feel free to install below plugins as you like:

1. [https://github.com/tailwindlabs/tailwindcss-typography](https://github.com/tailwindlabs/tailwindcss-typography)
1. [https://github.com/tailwindlabs/tailwindcss-forms](https://github.com/tailwindlabs/tailwindcss-forms)
1. [https://github.com/tailwindlabs/tailwindcss-aspect-ratio](https://github.com/tailwindlabs/tailwindcss-aspect-ratio)
1. [https://github.com/tailwindlabs/tailwindcss-line-clamp](https://github.com/tailwindlabs/tailwindcss-line-clamp)

## Form

To render Django form which work with tailwind, please check [https://github.com/django-crispy-forms/crispy-tailwind](https://github.com/django-crispy-forms/crispy-tailwind)
