.phony: create_venv code_quality

run:
	/usr/bin/env python3 summer_bumps.py

create_venv:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	
cq:
	autopep8 --in-place src/*.py ; \
	flake8 src/*.py ; \
	mypy src/*.py ; \
