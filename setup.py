import os
import re

from setuptools import find_packages, setup

from webpack_loader import GIT_URL


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    with open(os.path.join(package, "__init__.py")) as f:
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", f.read()).group(1)


def get_long_description():
    """
    Return the README.
    """
    with open("README.md", encoding="utf8") as f:
        return f.read()


setup(
    name="python-webpack-boilerplate",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=["cookiecutter",],
    version=get_version("webpack_loader"),
    description="Transparently use webpack with Python project",
    long_description=get_long_description(),
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
