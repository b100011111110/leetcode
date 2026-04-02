class Solution:
    def isSameAfterReversals(self, n: int) -> bool:
        if n == 0:
            return True
        return n%10 != 0