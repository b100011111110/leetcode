from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 99999999
        sol = 0
        for i in range(len(nums)):
            j,k = i+1,len(nums)-1
            while k > j:
                x = nums[i] + nums[j] + nums[k]
                if abs(x-target) < ans:
                    ans = abs(x-target)
                    sol = x
                if x == target:
                    return target
                elif x > target:
                    k -= 1
                elif x < target:
                    j += 1
        return sol