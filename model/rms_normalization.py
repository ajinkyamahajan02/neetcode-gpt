import numpy as np
from typing import List


class Solution:
    def rms_norm(self, x: List[float], gamma: List[float], eps: float) -> List[float]:
        
        x = np.array(x, dtype="float64")
        gamma = np.array(gamma, dtype="float64")
        rms = np.sqrt((np.mean(np.power(x, 2)) + eps))
        x_cap = x / rms
        return np.round((gamma * x_cap), 4).tolist()