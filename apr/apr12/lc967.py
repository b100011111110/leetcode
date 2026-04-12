from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        que = set(range(1,10))
        for i in range(n-1):
            nque = []
            for i in que:
                pd = i%10
                if pd + k < 10:
                    nque.append(i*10+pd + k)
                if pd - k >= 0:
                    nque.append(i*10+pd - k)
            que = set(nque)
        return list(que)