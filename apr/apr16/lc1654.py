from collections import deque
from typing import List

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        visited = set()
        que = deque()
        que.append((0, 0, False))  
        while que:
            s, n, back = que.popleft()
            if n == x:
                return s
            if not (0 <= n < 10000):
                continue
            if n in forbidden or (n, back) in visited:
                continue
            visited.add((n, back))
            que.append((s + 1, n + a, False))        
            if not back:
                que.append((s + 1, n - b, True))
        return -1