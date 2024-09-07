.phony: create_venv code_quality install run

install:
	.venv/bin/pip install .

run: install
	.venv/bin/summer_bumps

create_venv:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	
cq:
	autopep8 --in-place src/*.py ; \
	flake8 src/*.py ; \
	mypy src/*.py ; \
