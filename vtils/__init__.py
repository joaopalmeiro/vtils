# Source: https://github.com/python-poetry/poetry/pull/2366#issuecomment-652418094
import sys

from .pae import PAE

# More info:
# - https://github.com/bhrutledge/mypy-importlib-metadata
# - https://github.com/python/mypy/issues/1153
# - https://github.com/python/mypy/issues/1393

# try:
#     import importlib.metadata as importlib_metadata
# except ModuleNotFoundError:
#     import importlib_metadata

if sys.version_info[:2] >= (3, 8):
    import importlib.metadata as importlib_metadata
else:
    import importlib_metadata

__version__ = importlib_metadata.version(__name__)
