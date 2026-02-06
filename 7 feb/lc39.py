from typing import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        def traverse(sum,lst,k):
            if sum == target:
                ans.add(tuple(lst))
            if sum >= target:
                return
            for i in range(k,len(candidates)):
                sum += candidates[i]
                lst.append(candidates[i])
                traverse(sum,lst,i)
                lst.pop()
                sum -= candidates[i]
        traverse(0,[],0)
        return list(ans)
    
print(Solution().combinationSum([2,3,6,7],7))