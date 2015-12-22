CPYTHON_REPO = https://raw.githubusercontent.com/python/cpython/9378ca0

test:
	nosetests

original:
	mkdir -p original
	wget -q $(CPYTHON_REPO)/Parser/asdl.py -O original/asdl.py
	wget -q $(CPYTHON_REPO)/Lib/test/test_asdl_parser.py \
		-O original/test_asdl_parser.py
	wget -q $(CPYTHON_REPO)/Parser/Python.asdl -O original/Python.asdl
	wget -q $(CPYTHON_REPO)/LICENSE -O original/LICENSE

linter: original
	diff -u original/asdl.py asdl.py | pep8 --diff .
	diff -u original/test_asdl_parser.py test/test_asdl.py | pep8 --diff .
	pep8 --exclude=./original/,./asdl.py,./test/test_asdl.py .

dist-upload: linter test
	python setup.py sdist bdist_wheel
	twine upload dist/*

clean:
	rm -rf dist/ build/ *.egg-info/
	rm -rf original/

.PHONY: test linter dist-upload clean
