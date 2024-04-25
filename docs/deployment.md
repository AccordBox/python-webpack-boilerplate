# Deployment Notes

## Solution 1

On some platform such as Heroku, they have `buildpack` which can detect the project and deploy it automatically.

1. Please use `run_npm_command_at_root` to make sure the `package.json` exists at the root directory. [Run NPM command at root directory](run_npm_command_at_root.md)
1. Enable the `Javascript buildpack` on Heroku, so Heroku will detect `package.json` and run `npm run build` during the deployment. [Using Multiple Buildpacks for an App](https://devcenter.heroku.com/articles/using-multiple-buildpacks-for-an-app)
1. If you want to specify the version of `node`, `npm`, please check [https://devcenter.heroku.com/articles/nodejs-support#supported-runtimes](https://devcenter.heroku.com/articles/nodejs-support#supported-runtimes)

## Solution 2

Another solution is Docker, we can write code in `Dockerfile` to deploy.

One example file is on [https://github.com/AccordBox/django-heroku-docker/blob/master/Dockerfile](https://github.com/AccordBox/django-heroku-docker/blob/master/Dockerfile)
