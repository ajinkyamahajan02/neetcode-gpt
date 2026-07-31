import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List

class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        unique_words = []

        combined = positive + negative 

        for statement in combined: 
            words = statement.split(" ")
            for word in words:
                if word not in unique_words:
                    unique_words.append(word)

        unique_words = sorted(unique_words)

        start = 0
        wordMap = {}
        for word in unique_words:
            wordMap[word] = start + 1
            start = start+1

        pos_enc = []
        for statement in positive:
            words = statement.split(" ")
            enc = []
            for word in words:
                enc.append(wordMap[word])
            pos_enc.append(enc)

        neg_enc = []
        for statement in negative:
            words = statement.split(" ")
            enc = []
            for word in words:
                enc.append(wordMap[word])
            neg_enc.append(enc)


        encoded = []
        combined = pos_enc + neg_enc
        for enc in combined:
            encoded.append(torch.Tensor(enc))

        encoded = nn.utils.rnn.pad_sequence(encoded, batch_first=True)

        return encoded
        # 1. Build vocabulary: collect all unique words, sort them, assign integer IDs starting at 1
        # 2. Encode each sentence by replacing words with their IDs
        # 3. Combine positive + negative into one list of tensors
        # 4. Pad shorter sequences with 0s using nn.utils.rnn.pad_sequence(tensors, batch_first=True)
