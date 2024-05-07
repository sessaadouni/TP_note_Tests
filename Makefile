VENV_PATH = ./.venv
VENV_TOKEN = $(VENV_PATH)/.created

.PHONY: venv

venv: requirements.txt
	test -d $(VENV_PATH) || python3 -m venv $(VENV_PATH)
	. $(VENV_PATH)/bin/activate; pip install -Ur requirements.txt
	touch $(VENV_TOKEN)