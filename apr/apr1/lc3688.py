from typing import List

class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        nums = [i for i in nums if i%2 == 0]
        x = 0
        for i in nums:
            x |= i
        return x