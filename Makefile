.PHONY: unit unit-s integration integration-s tests install-pip install-virtualenv create-virtualenv purge-pyc develop

SHELL=/bin/bash

unit:
	@nosetests -c setup.cfg;

unit-s:
	@nosetests -s;

tests: unit

PIP_CHECK=$(shell dpkg -l python-pip | tail -n 1 | awk '{print $$1}')
install-pip:
	@if [ "$(PIP_CHECK)" = "No" -o "$(PIP_CHECK)" = "un" ]; then \
		echo "installing python-pip...password required for sudo"; \
		sudo apt-get install python-pip; \
	else \
		echo "python-pip already installed, skipping."; \
	fi

VIRTUALENV_CHECK=$(shell dpkg -l python-virtualenv | tail -n 1 | awk '{print $$1}')
install-virtualenv:
	@if [ "$(VIRTUALENV_CHECK)" = "No" -o "$(VIRTUALENV_CHECK)" = "un" ]; then \
		echo "installing python-virtualenv...password required for sudo"; \
		sudo apt-get install python-virtualenv; \
	else \
		echo "python-virtualenv already installed, skipping."; \
	fi

create-virtualenv:
	@if [ ! -d "virtualenv" ]; then \
		echo "creating new virtualenv..."; \
		virtualenv --distribute virtualenv; \
		echo "installing development requirements..."; \
		source virtualenv/bin/activate; \
		pip install -r requirements.txt; \
	else \
		echo "virtualenv already exists, skipping."; \
	fi

purge-pyc:
	find . -name "*.pyc" -delete;

develop: install-pip install-virtualenv create-virtualenv
