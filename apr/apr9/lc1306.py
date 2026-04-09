from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        que = deque()
        que.append(start)
        visited = set()
        while que:
            i = que.popleft()
            if not(0<=i<len(arr)):
                continue
            if arr[i] == 0:
                return True
            if i in visited:
                continue
            visited.add(i)
            que.append(i+arr[i])
            que.append(i-arr[i])
        return False