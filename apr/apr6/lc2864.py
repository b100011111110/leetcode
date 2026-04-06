class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        l = len(s)
        l1 = s.count('1')
        return '1' * (l1-1) + '0' * (l-l1) + '1'