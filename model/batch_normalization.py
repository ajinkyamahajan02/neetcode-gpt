import numpy as np
from typing import Tuple, List


class Solution:
    def batch_norm(self, x: List[List[float]], gamma: List[float], beta: List[float],
                   running_mean: List[float], running_var: List[float],
                   momentum: float, eps: float, training: bool) -> Tuple[List[List[float]], List[float], List[float]]:

        x = np.array(x, dtype="float64")
        gamma = np.array(gamma, dtype="float64")
        beta = np.array(beta, dtype="float64")
        running_mean = np.array(running_mean, dtype="float64")
        running_var = np.array(running_var, dtype="float64")

        if training:
            mean = np.mean(x, axis=0)
            var = np.var(x, axis=0)
            x_hat = (x - mean) / (np.sqrt(var + eps))
            running_mean = (1 - momentum) * running_mean + (momentum * mean)
            running_var = (1 - momentum) * running_var + (momentum * var)
            
        else:
            x_hat = (x - running_mean) / np.sqrt(running_var + eps)

        out = (x_hat * gamma) + beta
            
        
        return (np.round(out, 4).tolist(), 
        np.round(running_mean, 4).tolist(), 
        np.round(running_var, 4).tolist())
