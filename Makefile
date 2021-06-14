install-dev-deps: dev-deps
	pip-sync requirements.txt requirements-dev.txt

install-deps: deps
	pip-sync requirements.txt

deps:
	pip install --upgrade pip pip-tools
	pip-compile requirements.in

dev-deps: deps
	pip-compile requirements-dev.in

server:
	python manage.py migrate && python manage.py runserver

lint:
	flake8 django_boilerplate

black:
	python -m black django_boilerplate

cleanimports:
	autoflake -r -i --remove-all-unused-imports --ignore-init-module-imports django_boilerplate

checkmigrations:
	python manage.py makemigrations --check --no-input --dry-run

test:
	pytest -n 4 -x
