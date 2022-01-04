# Run NPM command at root directory

By default, the `package.json` will be placed at the `frontend` directory, which means, you need to run `npm` command under the `frontend` directory.

If you do not like this and want to run `npm` command at the root directory.

Please set `run_npm_command_at_root` to `y` when you create the `webpack` project.

Below files will be placed at the root directory instead of the `frontend` directory.

```
.babelrc
.browserslistrc
.eslintrc
.nvmrc
.stylelintrc.json
package-lock.json
package.json
```
