# vtils

A Python package providing utility functions for Data Visualization.

## Notes

- [pyenv](https://github.com/pyenv/pyenv):
  - `pyenv versions`.
  - `pyenv install 3.6.13`.
  - `pyenv global 3.6.13` (check with `pyenv global`).
- [Poetry](https://python-poetry.org/):
  - Install: `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`.
  - Uninstall: `curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | POETRY_UNINSTALL=1 python` ([source](https://github.com/python-poetry/poetry/issues/644)).
  - `poetry config virtualenvs.in-project true`.
  - `poetry config --list`.
  - `poetry init`.
  - `poetry --version`.
  - `poetry shell`.
  - Bump version: `poetry version patch` ([source](https://python-poetry.org/docs/cli/#version)).
  - Validate the `pyproject.toml` file: `poetry check`.
  - `poetry add numpy@^1.19.5`.
- [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme).
- [`numpy.typing`](https://numpy.org/devdocs/reference/typing.html):
  - NumPy 1.20.0.
  - [API](https://numpy.org/devdocs/reference/typing.html#api).
  - NumPy array: `np.ndarray`.
- Makefile:
  - "(...) variables defined with `:=` are expanded once, but variables defined with `=` are expanded whenever they are used." ([source](https://stackoverflow.com/a/4879613))
