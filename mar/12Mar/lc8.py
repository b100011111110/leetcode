class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0:
            return 0
        ans = '0'
        i = 0
        sign = 1
        while i < len(s) and s[i] not in '1234567890+-.':
            if s[i].isalpha():
                return 0
            i += 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            i += 1
            sign = -1
        while i < len(s) and s[i] in '1234567890':
            ans += s[i]
            i += 1
        num =  sign * int(ans)
        exp = 2 ** 31
        mx ,mi = exp-1,-1*exp
        if mx < num:
            return mx
        elif mi > num:
            return mi
        return num