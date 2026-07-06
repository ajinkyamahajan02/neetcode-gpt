import numpy as np
from numpy.typing import NDArray


class Solution:

    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x)) 
   
    def relu(self, x):
        return max(0.0, x)

    def forward(self, 
    x: NDArray[np.float64], 
    w: NDArray[np.float64], 
    b: float, 
    activation: str) -> float:
        pre_activation = np.matmul(w, x) + b

        if activation == "sigmoid":
            return np.round(self.sigmoid(pre_activation), 5)

        elif activation == "relu":
            return np.round(self.relu(pre_activation), 5)

        else:
            return pre_activation
