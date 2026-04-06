from typing import List

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        x = max(nums)
        return x * k + k*(k-1)//2