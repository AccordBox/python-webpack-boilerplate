When Webpacker compiles your JavaScript code, it scans the `src/application` directory for files with the .js extension and automatically includes them as entry points for the Webpack bundling process.

For the `application/app.js`, you can import it in template like this:

```
{% javascript_pack 'app' attrs='charset="UTF-8"' %}
```

In most cases, you do not need to create another file in this directory.
