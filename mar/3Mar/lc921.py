class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        c = 0
        a = 0
        for i in s:
            if i == '(':
                a += 1
            else:
                if a == 0:
                    c += 1
                else:
                    a -= 1
        return c+a