.PHONY: venv build

ENV := $(if $(env),$(env),staging)

venv:
	python -m venv .venv

build:
	python -m pip install --upgrade pip
	python -m pip install -e '.[generator]'


build-test:
	python -m pip install --upgrade pip
	python -m pip install -e '.[test]'

build-all: build build-test

init-infra:
	docker-compose up -d

shutdown:
	docker compose down