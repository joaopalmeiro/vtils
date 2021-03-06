# Source: https://github.com/trickeydan/cookiecutter-awesome-poetry
.PHONY: all type demo isort black lint bandit

CMD:=poetry run
PYMODULE:=vtils

all: type isort black lint bandit

type:
	$(CMD) mypy $(PYMODULE)

demo:
	$(CMD) jupyter notebook demo.ipynb

# No need for `--recursive`:
# https://pycqa.github.io/isort/docs/upgrade_guides/5.0.0/#-recursive-or-rc
isort:
	$(CMD) isort $(PYMODULE)

black:
	$(CMD) black $(PYMODULE)

lint:
	$(CMD) flake8 $(PYMODULE)

bandit:
	$(CMD) bandit -r $(PYMODULE)
