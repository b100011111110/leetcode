from typing import List
import math
from collections import defaultdict,deque

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n - 1):
            for j in range(i + 1, n):
                a = bombs[i]
                b = bombs[j]
                d = math.sqrt((a[0]-b[0]) ** 2 + (a[1]-b[1]) ** 2)
                if d <= a[2]:
                    graph[i].append(j)
                if d <= b[2]:
                    graph[j].append(i)
        ans = 0
        for i in range(n):
            que = deque([i])
            visited = set()
            c = 0
            while que:
                i = que.popleft()
                if i in visited:
                    continue
                visited.add(i)
                c += 1
                que.extend(graph[i])
            ans = max(ans, c)
        return ans