import os
import re

from setuptools import find_packages, setup
from webpack_loader import GIT_URL


def rel(*parts):
    """returns the relative path to a file wrt to the current directory"""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *parts))


README = open("README.md", "r").read()

with open(rel("webpack_loader", "__init__.py")) as handler:
    INIT_PY = handler.read()

VERSION = re.findall('__version__ = "([^\']+?)"', INIT_PY)[0]

setup(
    name="python-webpack-boilerplate",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=["cookiecutter",],
    version=VERSION,
    description="Transparently use webpack with Python project",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Michael Yin",
    author_email="michaelyin@accordbox.com",
    url=GIT_URL,
    keywords=["python", "django", "flask", "webpack"],  # arbitrary keywords
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
    ],
)
