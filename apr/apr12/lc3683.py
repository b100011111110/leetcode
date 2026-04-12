from typing import List

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        z = float('inf')
        for i,j in tasks:
            z = min(z,i+j)
        return z