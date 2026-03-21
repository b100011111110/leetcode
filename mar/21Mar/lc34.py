from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        n = len(nums)
        l,r = 0,n-1
        while r >= l:
            m = (l+r)//2
            if nums[m] >= target:
                r = m-1
            else:
                l = m+1
        if l >= n:
            return [-1,-1]
        if nums[l] != target:
            return [-1,-1]
        first = l
        l,r = 0,n-1
        while r >= l:
            m = (l+r)//2
            if nums[m] <= target:
                l = m+1
            else:
                r = m-1
        return [first,r]