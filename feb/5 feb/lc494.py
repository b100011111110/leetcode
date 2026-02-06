from typing import *
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {}
        def traverse(i,pv):
            if (i, pv) in self.memo:
                return self.memo[(i, pv)]
            if i == len(nums):
                if target == pv:
                    return 1
                return 0
            x = traverse(i+1,pv+nums[i])
            y = traverse(i+1,pv-nums[i])
            self.memo[(i, pv)] = x + y
            return self.memo[(i, pv)]
        return traverse(0,0)