from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 9999999
        j = 0
        sm = 0
        for i in range(len(nums)):
            sm += nums[i]
            while sm >= target:
                ans = min(ans, i - j + 1)
                sm -= nums[j]
                j += 1
        if ans == 9999999:
            return 0
        return ans