# Bootstrap

After you create the frontend project using this project

```bash
$ npm install bootstrap
```

Then you will see something like this in the package.json

```json
{
  "dependencies": {
    "bootstrap": "^5.3.0"
  }
}
```

Import Bootstrap in `src/application/app.js`

```javascript
import "bootstrap/dist/js/bootstrap.bundle";
```

Import Bootstrap SCSS in `src/styles/index.scss`

```scss
// If you comment out code below, bootstrap will use red as primary color
// and btn-primary will become red

// $primary: red;

@import "~bootstrap/scss/bootstrap.scss";
```

That is it, you can run `npm run watch` and check the result in the browser.

## Reference

[https://getbootstrap.com/docs/5.0/getting-started/webpack/](https://getbootstrap.com/docs/5.0/getting-started/webpack/)
