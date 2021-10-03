# Setup Vue

## Install

!!! note
    We will setup Vue 3 in this tutorial

Go to `frontend` directory

```bash
$ npm install vue-loader@16 @vue/compiler-sfc --save-dev
# install vue
$ npm install vue@3
```

You will have something like this in your `package.json`

```js
"vue-loader": "^16.8.1",
"@vue/compiler-sfc": "^3.2.19",

"vue": "^3.2.19"
```

Edit `frontend/webpack/webpack.common.js`

```js
const { VueLoaderPlugin } = require('vue-loader');

plugins: [
    ...

    new VueLoaderPlugin()
],

module: {
  rules: [
    ...
      
    {
      test: /\.vue$/,
      loader: "vue-loader",
    },
  ],
},
```

1. Add `VueLoaderPlugin` to `plugins`
1. Please also add rule to the `module.rules` to let webpack use `vue-loader` to process `.vue` files.

That is it, now the frontend project should work with Vue.

## Sample App

Create `frontend/src/components/HelloWorld.vue`

```vue
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    props: {
      msg: String
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
</style>
```

Create `frontend/src/components/App.vue`

```vue
<template>
  <div id="app">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import HelloWorld from './HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

In the `App.vue`, we import `HelloWorld.vue` and render it under `<div id="app">`

Edit `frontend/src/application/app2.js`

```js
import { createApp } from 'vue';
import App from '../components/App.vue';

createApp(App).mount('#app');
```

Now the file structures would seem like this:

```
src
├── application
│   ├── app.js
│   └── app2.js
├── components
│   ├── App.vue
│   ├── HelloWorld.vue
│   └── sidebar.js
└── styles
    └── index.scss
```

```
$ npm run start
```

Edit Django template `templates/index.html`

```django hl_lines="8 28"
{% load webpack_loader static %}

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Index</title>
  {% stylesheet_pack 'app' 'app2' %}
</head>
<body>

<div class="jumbotron py-5">
  <div class="container">
    <h1 class="display-3">Hello, world!</h1>
    <p>This is a template for a simple marketing or informational website. It includes a large callout called a
      jumbotron and three supporting pieces of content. Use it as a starting point to create something more unique.</p>
    <p><a class="btn btn-primary btn-lg" href="#" role="button">Learn more »</a></p>

    <div class="d-flex justify-content-center">
      <img src="{% static 'vendors/images/webpack.png' %}" class="img-fluid"/>
    </div>

  </div>
</div>

<div id="app"></div>

{% javascript_pack 'app' 'app2' %}

</body>
</html>
```

```bash
$ python manage.py runserver
```

!!! note
    Here we use Vue to render specific component in the page, and we can still use raw HTML to write other parts, which is convenient

![Vue example](images/vue-example.png)
