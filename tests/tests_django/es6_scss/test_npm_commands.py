import re


def test_npm(npm_project_path, npm_build_commands):
    js_path = npm_project_path / "build" / "js"
    js_files = list(js_path.glob("*.*"))
    js_files = [js_file.name for js_file in js_files]
    assert len(js_files) > 0
    js_files = ", ".join(js_files)
    assert re.findall(r"app[.\w]*?.js", js_files)
    assert re.findall(r"app2[.\w]*?.js", js_files)

    css_path = npm_project_path / "build" / "css"
    css_files = list(css_path.glob("*.*"))
    css_files = [css_file.name for css_file in css_files]
    assert len(css_files) > 0
    css_files = ", ".join(css_files)
    assert re.findall(r"app[.\w]*?.css", css_files)

    vendor_path = npm_project_path / "vendors" / "images"
    img_files = list(vendor_path.glob("*.*"))
    img_files = [img_file.name for img_file in img_files]
    assert len(img_files) > 0
    img_files = ", ".join(img_files)

    assert re.findall(r"sample.jpg", img_files)
    assert re.findall(r"webpack.png", img_files)
