from typing import *

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def generate(i,lst):
            if i == len(nums):
                ans.append(lst.copy())
                return
            generate(i+1,lst)
            lst.append(nums[i])
            generate(i+1,lst)
            lst.pop()
        generate(0,[])
        return ans
    
print(Solution().subsets([1,2]))