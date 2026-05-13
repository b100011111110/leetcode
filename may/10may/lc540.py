from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l,r = 0,len(nums)-1
        while r > l:
            m = (l+r)//2
            print(l,r,m)
            if nums[m] != nums[m+1] and nums[m] != nums[m-1]:
                return nums[m]
            if m%2 == 0:
                if nums[m] == nums[m+1]:
                    l = m
                else:
                    r = m
            else:
                if nums[m] == nums[m+1]:
                    r = m
                else:
                    l = m
        return -1
    
print(Solution().singleNonDuplicate([3,3,7,7,10,11,11]))