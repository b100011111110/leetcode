class Solution:
    def trailingZeroes(self, n: int) -> int:
        c = 0
        for i in range(1,n+1):
            n = i
            while n % 5 == 0:
                c += 1
                n //= 5
        return c