from typing import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest_index = 0
        for i in range(n):
            if i > farthest_index:
                return False
            farthest_index = max(farthest_index, i + nums[i])
            if farthest_index >= n-1:
                return True