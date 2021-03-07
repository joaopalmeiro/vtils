# vtils

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

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
  - Check plugins: `flake8 --version`.
  - Check `entry_points` in the `setup.py` (or `setup.cfg`) file for (default) error codes.
  - [Awesome Flake8 Extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions).
  - [flake8-docstrings](https://gitlab.com/pycqa/flake8-docstrings).
  - [flake8-commas](https://github.com/PyCQA/flake8-commas).
  - [flake8-import-order](https://github.com/PyCQA/flake8-import-order).
  - [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear).
    - "B006: Do not use mutable data structures for argument defaults."
  - [flake8-debugger](https://github.com/jbkahn/flake8-debugger).
  - [flake8-comprehensions](https://github.com/adamchainz/flake8-comprehensions).
  - [flake8-isort](https://github.com/gforcada/flake8-isort).
  - [flake8-mutable](https://github.com/ebeweber/flake8-mutable).
  - [flake8-todo](https://github.com/schlamar/flake8-todo).
  - [pep8-naming](https://github.com/PyCQA/pep8-naming).
  - [flake8-blind-except](https://github.com/elijahandrews/flake8-blind-except).
  - [flake8-builtins](https://github.com/gforcada/flake8-builtins).
  - [flake8-logging-format](https://github.com/globality-corp/flake8-logging-format).
  - [flake8-rst-docstrings](https://github.com/peterjc/flake8-rst-docstrings/).
  - [pandas-vet](https://github.com/deppen8/pandas-vet).
  - [flake8-simplify](https://github.com/MartinThoma/flake8-simplify).
- [Bandit](https://github.com/PyCQA/bandit):
  - Security linter.
  - [Codes](https://bandit.readthedocs.io/en/latest/plugins/index.html#complete-test-plugin-listing).
- Mypy:
  - [Missing type hints for third party library](https://mypy.readthedocs.io/en/latest/running_mypy.html#missing-type-hints-for-third-party-library).
- [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide).
