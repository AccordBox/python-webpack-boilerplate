.PHONY: docs

docs:
	mkdocs serve --dev-addr '127.0.0.1:9090'

build:
	poetry build

publish:
	poetry publish

# poetry config repositories.testpypi https://test.pypi.org/legacy/
publish-testpypi:
	poetry publish -r testpypi
