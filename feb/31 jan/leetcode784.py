from typing import *

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = s[::-1]
        def traverse(i):
            if i == -1:
                return ['']
            x = traverse(i-1)
            if ord('0') <= ord(s[i]) <= ord('9'):
                return [s[i]+j for j in x]
            lst = [s[i].lower()+j for j in x]
            lst.extend([s[i].upper()+j for j in x])
            return lst
        return traverse(len(s)-1)