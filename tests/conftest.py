import datetime
import os
import re
import signal
import subprocess

import pytest
from tests.config import NPM_BIN_PATH


def kill_process(name):
    """
    The web dev server can not be killed by process.kill()
    So we use this to kill the webpack dev server
    """
    try:
        for line in os.popen("ps -e | grep " + name + " | grep -v grep"):
            if "pytest" in line:
                # ignore
                continue
            fields = line.split()
            pid = fields[0]
            os.kill(int(pid), signal.SIGKILL)
        print("Process Successfully terminated")
    except Exception:
        print("Error Encountered while running script")


@pytest.fixture
def npm_project_path(tmp_path, request):
    from cookiecutter.main import cookiecutter

    base_dir = request.config.rootdir

    frontend_project_root = tmp_path
    cookiecutter(
        str(base_dir / "webpack_boilerplate" / "frontend_template"),
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

    # create another entrypoint file
    app_test_content = """
// This is a simple test script
console.log('Hello from app_test.js');
    """
    app_test_path = frontend_project_path / "src" / "application" / "app_test.js"
    app_test_path.write_text(app_test_content)

    yield frontend_project_path


@pytest.fixture(params=["start"])
def npm_build_commands(npm_project_path, request):
    kill_process("webpack")

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
    kill_process("webpack")
