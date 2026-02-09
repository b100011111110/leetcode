from typing import *
import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # this is heap sort
        x,ans = len(nums),[]
        heapq.heapify(nums)
        for i in range(x):
            ans.append(heapq.heappop(nums))
        return ans
    
print(Solution().sortArray([5,2,3,1]))