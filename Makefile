# Makefile

.PHONY: 

run: 
	python ./main.py

test: 
	coverage run -m unittest

coverage: test
	coverage report