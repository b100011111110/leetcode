from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def traverse(i,lst):
            if i == -1:
                return ['']
            ab = traverse(i-1,lst)
            ac = []
            for j in lst[i]:
                for k in ab:
                    ac.append(k+j)
            return ac
        x = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        lst = []
        for i in digits:
            lst.append(x[i])
        return traverse(len(lst)-1,lst)
    
