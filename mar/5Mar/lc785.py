from typing import *
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        for i in range(n):
            if color[i] == -1:
                que = deque([i])
                color[i] = 0
                while que:
                    node = que.popleft()
                    for j in graph[node]:
                        if color[j] == -1:
                            color[j] = 1 - color[node]
                            que.append(j)
                        elif color[j] == color[node]:
                            return False
        return True