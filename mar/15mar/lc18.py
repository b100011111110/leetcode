from typing import List 

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            for l in range(i+1,len(nums)):
                j,k = l+1,len(nums)-1
                while k > j:
                    print(i,l,j,k)
                    x = nums[i] + nums[j] + nums[k] + nums[l]
                    if x == target:
                        ans.add((nums[i] ,nums[l], nums[j] , nums[k]))
                        j += 1
                        k -= 1
                    elif x > target:
                        k -= 1
                    elif x < target:
                        j += 1
        return list(ans)
    
print(Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0))