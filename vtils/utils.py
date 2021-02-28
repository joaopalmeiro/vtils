import numpy as np


def head(array: np.ndarray, n: int = 5) -> np.ndarray:
    """Head-like function for NumPy arrays."""
    return array[:n]
