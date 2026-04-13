class Solution:
    def sumBase(self, n: int, k: int) -> int:
        c = 0
        while n:
            c += n%k
            n//=k
        return c