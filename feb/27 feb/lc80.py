from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        c,j = 1,0
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
                c = 1
            elif c == 1:
                j += 1
                nums[j] = nums[i]
                c = 2
        return j+1