.PHONY: venv build

ENV := $(if $(env),$(env),staging)

venv:
	python -m venv .venv

build:
	python -m pip install --upgrade pip
	python -m pip install -r container/fake_data_generator/requirements.txt


build-test:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

build-all: build build-test

infra-up:
	docker-compose up -d

infra-down:
	docker compose down

start: infra-down infra-up