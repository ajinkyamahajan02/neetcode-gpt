import numpy as np
from numpy.typing import NDArray
from typing import Tuple


class Solution:
    def backward(self, 
        x: NDArray[np.float64], 
        w: NDArray[np.float64], 
        b: float, 
        y_true: float) -> Tuple[NDArray[np.float64], float]:

        forward = np.matmul(x, w) + b
        z = 1.0 / (1.0 + np.exp(-forward))

        loss = np.power((z - y_true), 2) / 2.0

        gradient = np.dot((z - y_true), np.dot(np.dot(z, (1 - z)), x))
        gradient_db = np.dot((z - y_true), np.dot(z, (1 - z)))

        return (np.round(gradient, 5), np.round(gradient_db, 5))