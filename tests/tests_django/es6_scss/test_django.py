import re


def test_django(settings, npm_project_path, npm_build_commands):
    settings.STATICFILES_DIRS = [str(npm_project_path / "build")]

    settings.WEBPACK_LOADER = {
        "MANIFEST_FILE": str(npm_project_path / "build" / "manifest.json"),
    }

    from webpack_loader.templatetags.webpack_loader import (
        javascript_pack,
        stylesheet_pack,
    )

    html = javascript_pack("app", "app2")
    assert re.findall(r"app[.\w]*?.js", html)
    assert re.findall(r"app2[.\w]*?.js", html)
    # also load dependency
    assert len(re.findall(r"<script", html)) > 2

    html = stylesheet_pack("app")
    assert re.findall(r"app[.\w]*?.css", html)
