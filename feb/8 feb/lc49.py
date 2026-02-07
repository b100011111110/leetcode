from typing import *
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = DefaultDict(list)
        for i in strs:
            key = ''.join(sorted(i))
            x[key].append(i)
        return [x[i] for i in x]