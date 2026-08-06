from typing import List


class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        
        merges = []
        chs = list(corpus)
        
        for _ in range(num_merges):
            if len(chs) < 2:
                break
            
            pairs = {}
            for i in range(len(chs)-1):
                pair = (chs[i], chs[i+1])
                pairs[pair] = pairs.get(pair, 0) + 1
            
            if not pairs:
                break
            
            best_count = max(pairs.values())
            candidates = sorted(p for p, c in pairs.items() if c == best_count)

            best = candidates[0]
            merges.append([best[0], best[1]])

            new_tokens = []
            i = 0

            while i < len(chs):
                if i < len(chs) - 1 and chs[i] == best[0] and chs[i+1] == best[1]:
                    new_tokens.append(best[0] + best[1])
                    i += 2
                else:
                    new_tokens.append(chs[i])
                    i += 1
            chs = new_tokens

        return merges
