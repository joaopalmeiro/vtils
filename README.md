# vtils

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

A Python package providing utility functions for Data Visualization.

## References

- G. Ryan, A. Mosca, R. Chang and E. Wu, "At a Glance: Pixel Approximate Entropy as a Measure of Line Chart Complexity," in **_IEEE Transactions on Visualization and Computer Graphics_**, vol. 25, no. 1, pp. 872-881, Jan. 2019, doi: 10.1109/TVCG.2018.2865264.
- [`pae`](https://github.com/cudbg/pae) package.

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
- [Black compatible configurations](https://black.readthedocs.io/en/stable/compatible_configs.html).
- isort:
  - Check isort config: `isort . --show-config`.
  - [Black](https://black.readthedocs.io/en/stable/compatible_configs.html#isort).
- Flake8:
  - [Black](https://black.readthedocs.io/en/stable/compatible_configs.html#flake8).
  - Check the list of error codes ignored by default: `flake8 --help` (`--ignore`).
  - [flake8-docstrings](https://gitlab.com/pycqa/flake8-docstrings).
- [Bandit](https://github.com/PyCQA/bandit):
  - Security linter.
  - [Codes](https://bandit.readthedocs.io/en/latest/plugins/index.html#complete-test-plugin-listing).
