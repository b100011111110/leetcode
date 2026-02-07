from typing import *

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(n):
            c,p = 0,0
            if n == 0:
                return mapping[0]
            while n:
                d = n % 10
                n //= 10
                c += mapping[d] * 10 ** p 
                p += 1
            return c
        conv = {i:convert(i) for i in nums}
        return sorted(nums,key=lambda i : conv[i])