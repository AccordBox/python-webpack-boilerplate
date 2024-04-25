# Change Log

## v1.0.3

1. Remove `Bootstrap` from the default setup.
2. Update doc about `Bootstrap`, `SWC`, `React`, `Vue`
3. Update frontend dependency to the latest version

## v1.0.2

1. Support Node LTS Iron
2. Upgrade some frontend dependency
3. Switch from `@babel/plugin-proposal-class-properties` to `@babel/plugin-transform-class-properties`

## v1.0.1

1. Upgrade some frontend dependency

## v1.0.0

1. Upgrade nearly all frontend dependency package.
1. Drop `file-loader`, use `Webpack Asset` instead
1. Remove deprecated package `babel/polyfil`
1. Update Tailwind doc for v3

## v0.0.10

1. Fix `stylelint` when `run_npm_command_at_root`

## v0.0.9

1. Fix missing `postcss.config.js` when `run_npm_command_at_root`

## v0.0.8

1. Drop IE support in `browserslist`
1. Add `run_npm_command_at_root`, so user can run `npm` command under the root directory instead of the `frontend` directory.
1. Add `esbuild` support in doc
1. Add `live reload` feature in doc

## v0.0.7

1. Makes `webpack_loader` render Django hashed static file
1. Update `pre-commit-config.yaml`

## v0.0.6

DELETED

## v0.0.5

1. Use `Poetry` to manage project meta info and dependency
1. Rename app from `webpack_loader` to `webpack_boilerplate`
1. Move the `frontend_template` under `webpack_boilerplate` directory
1. When publishing, upload `frontend_template` so the frontend template is also pinned.
1. Make `cookiecutter` use `frontend_template` in `webpack_boilerplate` directory instead of the Git repo.

## v0.0.4

1. Upgrade nvmrc to use `lts/fermium`
1. Upgrade dependency
1. Import `postcss-preset-env`
1. Add doc for `Tailwind CSS`

## v0.0.3

1. Update README
1. Better support JS debug
