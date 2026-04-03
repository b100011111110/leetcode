from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a,b = 0,0
        for i in nums:
            a += i
            c = i
            while c:
                b += c%10
                c//=10
        return a-b