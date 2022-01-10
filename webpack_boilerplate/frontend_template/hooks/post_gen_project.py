import os
import os.path
import shutil

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

DENY_LIST = [".gitignore"]
ALLOW_LIST = ["package.json", "package-lock.json", "postcss.config.js"]


def print_success_msg(msg):
    print(SUCCESS + msg + TERMINATOR)


def get_frontend_config_files():
    frontend_path = os.getcwd()

    for f in os.listdir(frontend_path):
        if f.startswith(".") and f not in DENY_LIST:
            full_path = os.path.join(frontend_path, f)
            yield os.path.dirname(full_path), os.path.basename(full_path)

    for f in ALLOW_LIST:
        full_path = os.path.join(frontend_path, f)
        yield os.path.dirname(full_path), os.path.basename(full_path)


def copy_frontend_config_files():
    for dirname, filename in get_frontend_config_files():
        old_full_path = os.path.join(dirname, filename)
        root_dir = os.path.dirname(dirname)
        new_full_path = os.path.join(root_dir, filename)
        shutil.copyfile(old_full_path, new_full_path)

        os.remove(old_full_path)


def update_webpack_path():
    """
    Update webpack config file path in package.json
    """
    file_path = "package.json"
    with open(file_path, "r+") as f:
        file_contents = f.read().replace(
            "--config webpack/", "--config {{ cookiecutter.project_slug }}/webpack/"
        )
        f.seek(0)
        f.write(file_contents)
        f.truncate()


def main():
    if "{{ cookiecutter.run_npm_command_at_root }}".lower() == "y":
        update_webpack_path()
        copy_frontend_config_files()

    print_success_msg(
        f"Frontend app '{{ cookiecutter.project_slug }}' "
        f"has been created. "
        f"To know more, check https://python-webpack-boilerplate.rtfd.io/en/latest/frontend/"
    )


if __name__ == "__main__":
    main()
