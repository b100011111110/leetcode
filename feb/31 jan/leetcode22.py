from typing import *

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        x = {1:['()'],0:[]}
        def backtrack(n):
            if n == 0 or n == 1:
                return
            backtrack(n-1)
            lst = set()
            for i in x[n-1]:
                lst.add(f'({i})')    
            for i in range(1,n):
                for j in x[i]:
                    for k in x[n-i]:
                        lst.add(j+k)
            x[n] = lst
        backtrack(n)
        return x[n]
    
print(Solution().generateParenthesis(3)[3])