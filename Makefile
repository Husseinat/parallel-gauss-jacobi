install:
	echo "Installing numpy for python3"
	python3 -m pip install --user numpy

run:
	echo "System is initializing"
	python3 main.py

test:
	echo "Running tests"
	python3 main.py < tests/1.in
