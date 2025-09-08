    .PHONY: test ci fmt

    VENV?=.venv
    PY?=$(VENV)/bin/python
    PIP?=$(VENV)/bin/pip

    $(VENV)/bin/activate:
	python3 -m venv $(VENV)
	$(PIP) install -U pip
	$(PIP) install -r requirements.txt

    fmt:
	pre-commit run -a || true

    test: $(VENV)/bin/activate
	$(PY) scripts/validate.py
	$(PY) scripts/check_cycles.py

    ci: test
	@echo 'CI checks passed.'
