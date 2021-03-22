import re
import datetime
import subprocess

import pytest

from tests.config import NPM_BIN_PATH


@pytest.fixture
def npm_project_path(tmp_path, request):
    from cookiecutter.main import cookiecutter

    base_dir = request.config.rootdir

    frontend_project_root = tmp_path
    cookiecutter(
        str(base_dir / "frontend_template"),
        no_input=True,
        output_dir=str(frontend_project_root),
    )

    frontend_project_path = frontend_project_root / "frontend"

    command = [NPM_BIN_PATH, "install"]
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        cwd=str(frontend_project_path),
    )
    print(result.stdout, result.stderr)

    yield frontend_project_path


@pytest.fixture(params=["start", "watch", "build"])
def npm_build_commands(npm_project_path, request):
    command = [NPM_BIN_PATH, "run", request.param]
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=str(npm_project_path),
    )
    run_time = datetime.datetime.now()
    while True:
        output = process.stdout.readline().decode("utf-8")
        if output:
            print(output.strip())
        if re.findall(r"webpack ([\d.]+) compiled (.+?) in (\d+) ms", output):
            break
        if datetime.datetime.now() - run_time > datetime.timedelta(seconds=60):
            # if the webpack not finish in 60 seconds
            raise Exception("Webpack compile failed")

    yield

    # kill the npm command
    process.kill()
