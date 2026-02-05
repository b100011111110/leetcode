from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        a = Counter(s)
        return ''.join(sorted(s,key = lambda i : (a[i],i),reverse=True))