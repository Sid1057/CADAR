all: clean build test gen_docs

clean:
	echo clean Cython compiled files
	rm -f CADAR/*.c*
	rm -rf build
	echo

build: CADAR/*.pyx
	python3 setup.py build_ext --inplace
	echo

test: CADAR/*.pyx test/*.py *
	echo Syntax checking via flake8
	flake8 CADAR/*.pyx test/*.py
	
	echo Type checking via mypy
	mypy --scripts-are-modules CADAR/*.pyx
	mypy --follow-imports normal --namespace-packages --pretty test/*.py
	
	echo API test
	python3 test/simple_test.py
	
	echo

gen_docs:
	echo Generating cython docs
	cython -a -3 CADAR/*.pyx
	mv CADAR/*.html docs/cython/
	echo
