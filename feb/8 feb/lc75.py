from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        le = len(nums)
        l,r,i = 0,le-1,0
        while i <= r:
            if  nums[i] == 0:
                nums[l],nums[i] = nums[i],nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r],nums[i] = nums[i],nums[r]
                r -= 1 
            else:
                i += 1