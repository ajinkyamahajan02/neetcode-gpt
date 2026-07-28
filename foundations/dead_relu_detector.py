import torch
import torch.nn as nn
from typing import List


class Solution:

    def detect_dead_neurons(self, model: nn.Module, x: torch.Tensor) -> List[float]:

        dead_fracs = []

        with torch.no_grad():
            for module in model.children():
                x = module(x)
                if isinstance(module, nn.ReLU):
                    dead_frac = round(((x == 0).all(dim=0)).float().mean().item(), 4)
                    dead_fracs.append(dead_frac)
        return dead_fracs

    def suggest_fix(self, dead_fractions: List[float]) -> str:

        if len(dead_fractions) == 0:
            return 'healthy'

        max_frac = max(dead_fractions)
        if max_frac > 0.5:
            return 'use_leaky_relu'

        if dead_fractions[0] > 0.3:
            return 'reinitialize'

        if (len(dead_fractions) >= 2
            and dead_fractions == sorted(dead_fractions)
            and dead_fractions[-1] > 0.1
        ):
            return 'reduce_learning_rate'

        if max_frac < 0.1:
            return 'healthy'

        return 'healthy'