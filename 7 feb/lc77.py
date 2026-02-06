from typing import *

class Solution:
    def combine(self, n: int, kk: int) -> List[List[int]]:
        ans = []
        candidates = list(range(1,n+1))
        depth = kk
        def traverse(level,lst,k):
            if level == depth:
                ans.append(tuple(lst))
                return
            for i in range(k,len(candidates)):
                level += 1
                lst.append(candidates[i])
                traverse(level,lst,i+1)
                lst.pop()
                level -= 1
        traverse(0,[],0)
        return ans
    
print(Solution().combine(4,2))