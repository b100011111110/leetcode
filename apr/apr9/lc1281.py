class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a,b = 0,1
        while n:
            c = n%10
            a += c
            b *= c
            n //= 10
        return b-a