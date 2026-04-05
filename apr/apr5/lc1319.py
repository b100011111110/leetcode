from collections import defaultdict, deque
from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        edges = len(connections)
        if n-1 > edges:
            return -1
        visited = set()
        graph = defaultdict(list)
        for i,j in connections:
            graph[i].append(j)
            graph[j].append(i)
        parts = 0
        for i in range(n):
            if i not in visited:
                parts += 1
                que = deque([i])
                while que:
                    node = que.popleft()
                    if node in visited:
                        continue
                    visited.add(node)
                    que.extend([i for i in graph[node] if i not in visited])
        return edges - parts