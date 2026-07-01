import numpy as np

class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:

        minimize = init

        for _ in range (iterations):
            minimize = minimize - (learning_rate * 2 * minimize)

        return np.round(minimize, 5)
        