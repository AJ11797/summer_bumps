.phony: create_venv code_quality install run

install:
	.venv/bin/pip install .

run: install
	.venv/bin/summer_bumps

create_venv:
	python3 -m venv .venv
	.venv/bin/pip install -r dev_requirements.txt
	
cq:
	autopep8 --in-place src/summer_bumps/*.py ; \
	flake8 src/summer_bumps/*.py ; \
	mypy src/summer_bumps/*.py ; \
