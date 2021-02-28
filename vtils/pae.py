import numpy as np


class ApproximateEntropy:
    def __init__(self, m: int = 2, r: float = 20.0) -> None:
        self.m = m
        self.r = r

    @staticmethod
    def _distance():
        pass

    @staticmethod
    def _phi(N, m, r, data):
        W = N - m + 1
        s = np.empty((W, m))

        # HERE

    def compute(self, data):
        N = data.shape[0]

        phi_m = self._phi(N, self.m, self.r, data)
