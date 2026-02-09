from typing import * 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans,used = [],[0] * len(nums)
        def backtrack(i,lst):
            if i == len(nums):
                ans.append(tuple(lst))
            for j in range(len(nums)):
                if used[j] == 0:
                    used[j] = 1
                    lst.append(nums[j])
                    backtrack(i+1,lst)
                    used[j] = 0
                    lst.pop()
        backtrack(0,[])
        return ans
    
print(Solution().permute([1,2,3]))