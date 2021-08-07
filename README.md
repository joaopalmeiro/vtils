# vtils

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python package providing utility functions for Data Visualization.

## References

- G. Ryan, A. Mosca, R. Chang and E. Wu, "At a Glance: Pixel Approximate Entropy as a Measure of Line Chart Complexity," in **_IEEE Transactions on Visualization and Computer Graphics_**, vol. 25, no. 1, pp. 872-881, Jan. 2019, doi: 10.1109/TVCG.2018.2865264.
- [`pae`](https://github.com/cudbg/pae) package.
- [`colormath`](https://github.com/gtaylor/python-colormath) package.

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
  - `classifiers`:
    - Python classifiers are added automatically from the `python` requirement. In `vtils`:
      - Programming Language :: Python :: 3
      - Programming Language :: Python :: 3.6
      - Programming Language :: Python :: 3.7
      - Programming Language :: Python :: 3.8
      - Programming Language :: Python :: 3.9
    - The `license` property will also set the License classifier automatically. In `vtils`:
      - License :: OSI Approved :: MIT License
  - [Add zip_safe support](https://github.com/python-poetry/poetry/issues/928) (open) issue.
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
  - [flake8-colors](https://github.com/and3rson/flake8-colors).
- [Bandit](https://github.com/PyCQA/bandit):
  - Security linter.
  - [Codes](https://bandit.readthedocs.io/en/latest/plugins/index.html#complete-test-plugin-listing).
  - [bandit linter messages don't appear in the "Problems" tab](https://github.com/microsoft/vscode-python/issues/15561) (open) issue.
- Mypy:
  - [Missing type hints for third party library](https://mypy.readthedocs.io/en/latest/running_mypy.html#missing-type-hints-for-third-party-library).
  - [Making PEP 561 compatible packages](https://mypy.readthedocs.io/en/stable/installed_packages.html#making-pep-561-compatible-packages).
- [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide).

### Color difference

- [Wikipedia page](https://en.wikipedia.org/wiki/Color_difference).
- Euclidean distance for RGB colors and perceptually-uniform color spaces.
- sRGB is not perceptually uniform.
- Delta E [equations](https://python-colormath.readthedocs.io/en/latest/delta_e.html) (distance metrics):
  - **CIE76**: Euclidean distance between two points in [CIELAB/Lab](https://en.wikipedia.org/wiki/CIELAB_color_space) color space.
    - ≈ 2.3 corresponds to a JND (just noticeable difference) [for most Delta E equations](https://colorjs.io/docs/color-difference.html#delta-e-%CE%B4e).
  - **CIE94**: It accommodates perceptual non-uniformities through the use of application-specific weights.
    - The first color is the reference color (CIE94 is not symmetric).
  - **CIEDE2000**: It is a major revision of CIE94 with five corrections.
  - **CMC**/**CMC(l:c)** (1984): It was developed by the Colour Measurement Committee of the Society of Dyers and Colourists.
    - The first color is the reference color (CMC is not symmetric).
    - It has two parameters: lightness (`l`) and chroma (`c`). They allow the users to weight the difference based on the ratio of `l:c` that is deemed appropriate. The usual values are `2:1` for "acceptability" and `1:1` for "imperceptibility".
- CIE: International Commission on Illumination.
- Gamut: Range of colors.
- [Colour](https://github.com/colour-science/colour) package.
- [`d3-color-difference`](https://github.com/Evercoder/d3-color-difference) package.
- [LuxPy](https://github.com/ksmet1977/luxpy) package ([documentation](http://ksmet1977.github.io/luxpy/)).
- [`color`](https://scikit-image.org/docs/stable/api/skimage.color.html) module ([`scikit-image`](https://scikit-image.org/) package).
- [Color.js](https://github.com/LeaVerou/color.js) package.

## Snippets

Check the Python implementation ([source](https://stackoverflow.com/a/14718168)):

```python
import platform

platform.python_implementation()
```
