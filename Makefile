# Source: https://github.com/trickeydan/cookiecutter-awesome-poetry.
.PHONY: all type

CMD:=poetry run
PYMODULE:=vtils

all: type

type:
	$(CMD) mypy $(PYMODULE)
