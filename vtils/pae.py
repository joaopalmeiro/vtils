import numpy as np


class ApproximateEntropy:
    def __init__(self, m: int = 2, r: float = 20.0) -> None:
        self.m = m
        self.r = r

    @staticmethod
    def _phi(N: int, m: int, r: float, data: np.ndarray) -> float:
        W = N - m + 1
        windows = np.empty((W, m))

        for i in range(W):
            windows[i, :] = data[i : i + m]

        # Similarities for each window.
        S = np.zeros(W)
        for i in range(W):
            # `axis=1`: maxima along the second axis.
            # Each window of size m is compared with every other window of the same size.
            distance = np.max(np.abs(windows - np.roll(windows, i, axis=0)), axis=1)
            S += np.less_equal(distance, r)
        S /= W

        # `.item()`: return Python float.
        return (W ** (-1) * np.sum(np.log(S))).item()

    def compute(self, data: np.ndarray) -> float:
        if data.ndim != 1:
            raise ValueError("The input data must be 1D.")

        N = data.shape[0]

        phi_m = self._phi(N, self.m, self.r, data)
        phi_m_plus_one = self._phi(N, self.m + 1, self.r, data)

        return abs(phi_m - phi_m_plus_one)


class Scaler:
    def __init__(self, w: int, h: int) -> None:
        self.h = h
        self.w = w

    def scale(self, data: np.ndarray):
        pass
