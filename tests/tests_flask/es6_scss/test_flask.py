import re


def test_flask(config, npm_project_path, npm_build_commands):
    config.update(
        {
            "static_folder": str(npm_project_path / "build"),
            "WEBPACK_LOADER": {
                "MANIFEST_FILE": str(npm_project_path / "build" / "manifest.json"),
            },
        }
    )

    from webpack_loader.contrib.jinja2ext import javascript_pack, stylesheet_pack

    html = javascript_pack("app", "app2")
    assert re.findall(r"app[.\w]*?.js", html)
    assert re.findall(r"app2[.\w]*?.js", html)
    # also load dependency
    assert len(re.findall(r"<script", html)) > 2

    html = stylesheet_pack("app")
    assert re.findall(r"app[.\w]*?.css", html)
