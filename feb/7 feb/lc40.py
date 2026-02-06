from typing import *
from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = dict(Counter(candidates))
        candidates = [[i,candidates[i]] for i in candidates]
        def traverse(sum,lst,k):
            if sum == target:
                ans.append(tuple(lst))
            if sum >= target:
                return
            for i in range(k,len(candidates)):
                if candidates[i][1] != 0:
                    candidates[i][1] -= 1
                    sum += candidates[i][0]
                    lst.append(candidates[i][0])
                    p = i+1 if candidates[i][1] == 0 else i
                    traverse(sum,lst,p)
                    lst.pop()
                    sum -= candidates[i][0]
                    candidates[i][1] += 1
        traverse(0,[],0)
        return ans
    
print(Solution().combinationSum2([10,1,2,7,6,1,5],8))