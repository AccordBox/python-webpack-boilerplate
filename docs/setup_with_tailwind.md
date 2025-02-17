# Tailwind CSS v4

From `python-webpack-boilerplate>=1.0.4`, we can choose `tailwind` as the style solution when creating the frontend project.

```bash
(venv) python manage.py webpack_init
  [1/3] project_slug (frontend):
  [2/3] run_npm_command_at_root (y):
  [3/3] Select style_solution
    1 - tailwind
    2 - bootstrap
    3 - scss
    Choose from [1/2/3] (1): 1
 [SUCCESS]: Frontend app 'frontend' has been created. To know more, check https://python-webpack-boilerplate.rtfd.io/en/latest/frontend/
```

Just choose `tailwind` as the style_solution, the Tailwind V4 will be ready for you.

## Install Dependency

In directory which contains the `package.json`

```bash
# install dependency packages
$ npm install
# run webpack in watch mode
$ npm run watch
```

## Explicitly Specify Source Files

Even Tailwind 4 can AUTO scan all project files in the project directory, we still recommend to explicitly specify the source files to improve performance and avoid webpack keeps recompiling.

Below is an example

```css
/*import tailwindcss and disable automatic source detection*/
@import "tailwindcss" source(none);

/*register frontend directory*/
@source "../";

/*register django templates*/
@source "../../../django_tailwind_app/**/*.html";

.jumbotron {
    /*should be relative path of the entry css file*/
    background-image: url("../../vendors/images/sample.jpg");
    background-size: cover;
}

@layer components{
    .btn-blue {
        @apply inline-flex items-center;
        @apply px-4 py-2;
        @apply font-semibold rounded-lg shadow-md;
        @apply text-white bg-blue-500;
        @apply hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400/50;
    }
}
```

!!! note
    Please remember to update the file path in your project.

## Live Reload

[Live Reload Support](live_reload.md)

## Tailwind V3

If you still want to install Tailwind V3, please check [Tailwind CSS v3](setup_with_tailwind3.md)
