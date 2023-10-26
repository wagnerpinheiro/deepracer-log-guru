var_temp := x

# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

setup:
	python -m venv .env

config:
	. .env/bin/activate && \
	pip3 install -r requirements.txt

install:
	brew install python-tk
	. .env/bin/activate && \
	pip3 install matplotlib==3.3.3 numpy==1.19.3 scipy==1.6.0

run: ## run
	. .env/bin/activate && \
	python3 -m src.main.guru