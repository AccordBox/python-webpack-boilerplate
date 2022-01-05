# Change Log

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
