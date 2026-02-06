from typing import *

class Solution:
    def combinationSum3(self, kk: int, n: int) -> List[List[int]]:
        ans = []
        candidates = list(range(1,10))
        depth = kk
        target = n
        def traverse(level,lst,k,sum):
            if level > depth or sum > target:
                return
            if level == depth and sum == target:
                ans.append(tuple(lst))
                return
            for i in range(k,len(candidates)):
                level += 1
                sum += candidates[i]
                lst.append(candidates[i])
                traverse(level,lst,i+1,sum)
                sum -= candidates[i]
                lst.pop()
                level -= 1
        traverse(0,[],0,0)
        return ans
    
print(Solution().combinationSum3(3,7))