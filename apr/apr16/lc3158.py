from typing import List

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i]+=1
        xor = 0
        for i in dic.keys():
            if dic[i] == 2:
                xor^=i
        return xor