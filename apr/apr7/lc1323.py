class Solution:
    def maximum69Number (self, num1: int) -> int:
        num = str(num1)
        if '6' in num:
            i = num.index("6")
            num = num[:i] + "9" + num[i+1:]
        return int(num)