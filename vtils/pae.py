import numpy as np


class ApproximateEntropy:
    def __init__(self, m: int = 2, r: float = 20.0) -> None:
        self.m = m
        self.r = r

    @staticmethod
    def _distance():
        pass

    @staticmethod
    def _phi(N: int, m: int, r: float, data: np.ndarray):
        W = N - m + 1
        windows = np.empty((W, m))

        for i in range(W):
            windows[i, :] = data[i : i + m]

        S = np.zeros(W)
        # HERE

    def compute(self, data: np.ndarray):
        if data.ndim != 1:
            raise ValueError("The input data must be 1D.")

        N = data.shape[0]

        phi_m = self._phi(N, self.m, self.r, data)
