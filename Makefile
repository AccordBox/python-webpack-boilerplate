.PHONY: clean build publish

clean:
	@echo "Cleaning..."
	@find webpack_loader/ -name '*.pyc' -delete
	@rm -rf ./build ./*egg* ./.coverage ./dist

build: clean
	@echo "Building..."
	@pip install -U setuptools
	@python setup.py sdist bdist_wheel --universal

publish: build
	@echo "Publishing to pypi..."
	@twine upload dist/*

publish_test: build
	@echo "Publishing to test pypi..."
	@twine upload --repository testpypi dist/*
