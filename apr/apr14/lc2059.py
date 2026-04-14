from collections import deque
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        que = deque()
        que.append((0,start))
        visited = set()
        while que:
            s,n = que.popleft()
            if n == goal:
                return s
            if n in visited or n >= 1000 or n < 0:
                continue
            visited.add(n)
            for i in nums:
                que.append((s+1,n+i))
                que.append((s+1,n-i))
                que.append((s+1,n^i))
        return -1

print(Solution().minimumOperations([2,4,12], 2, 12))
print(Solution().minimumOperations([3,5,7], 0, -4))
print(Solution().minimumOperations([2,8,16], 0, 1))
