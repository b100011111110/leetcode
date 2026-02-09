from typing import *
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        counter = [[i,counter[i]] for i in counter]
        ans = []
        def backtrack(i,lst):
            if i == len(nums):
                ans.append(tuple(lst))
            for j in range(len(counter)):
                if counter[j][1] != 0:
                    counter[j][1] -= 1
                    lst.append(counter[j][0])
                    backtrack(i+1,lst)
                    lst.pop()
                    counter[j][1] += 1
        backtrack(0,[])
        return ans
    
print(Solution().permuteUnique([1,1,2]))