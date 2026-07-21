import numpy as np
from numpy.typing import NDArray


class Solution:
    def forward(self, x: NDArray[np.float64], gamma: NDArray[np.float64], beta: NDArray[np.float64]) -> NDArray[np.float64]:

        mean = np.mean(x)
        var = np.mean(np.power((x - mean), 2))
        eps = 1e-5

        layer_norm = (gamma * ((x - mean) / np.sqrt(var + eps)) + beta)
        return np.round(layer_norm, 5)