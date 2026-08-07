from typing import Dict, List, Tuple

class Solution:
    def build_vocab(self, text: str) -> Tuple[Dict[str, int], Dict[int, str]]:

        stoi = {}
        curr = 0

        for ch in sorted(list(text)):
            if ch not in stoi.keys():
                stoi[ch] = curr
                curr += 1
        
        itos = {value: key for key, value in stoi.items()}

        print(stoi)
        return (stoi, itos)


    def encode(self, text: str, stoi: Dict[str, int]) -> List[int]:

        int_map = []
        for ch in text:
            int_map.append(stoi[ch])

        return int_map

    def decode(self, ids: List[int], itos: Dict[int, str]) -> str:

        text = ""
        for element in ids:
            text += str(itos[element])

        return text
