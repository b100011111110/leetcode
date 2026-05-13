from typing import List
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = Counter(nums)
        n = max(c)
        ans = [0] * (n + 1)
        ans[1] = c[1]
        for i in range(2,n+1):
            ans[i] = max(ans[i-1],i*c[i]+ans[i-2])
        return ans[-1]