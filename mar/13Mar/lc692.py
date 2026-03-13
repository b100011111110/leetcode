from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        x = Counter(words)
        return sorted(x.keys(),key = lambda i:(-x[i],i))[:k]