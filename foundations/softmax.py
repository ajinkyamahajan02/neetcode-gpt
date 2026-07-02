import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:

        max_z = max(z)
        summation = np.sum(np.exp(z - max_z))

        return np.round(np.exp(z - max_z) / summation, 4)
