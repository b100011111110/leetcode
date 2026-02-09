from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        x = defaultdict(int)
        for i in range(len(order)):
            x[order[i]] = i
        return ''.join(sorted(s,key = lambda i : x[i]))