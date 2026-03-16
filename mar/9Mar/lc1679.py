from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        x = Counter(nums)
        ans = 0
        for i in x:
            if k-i in x:
                ans += min(x[i],x[k-i])
        return ans//2