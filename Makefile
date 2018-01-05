VENV_NAME := .env

all: build

build: .build.ts

run: build
	$(VENV_NAME)/bin/python run.py

run_with_appd: build
	$(VENV_NAME)/bin/pyagent run -c appd.config -- $(VENV_NAME)/bin/python run.py

.build.ts:
	python3 -m venv $(VENV_NAME)
	$(VENV_NAME)/bin/pip install -r requirements.txt
	@touch $@
