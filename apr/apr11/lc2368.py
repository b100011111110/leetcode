from typing import List
from collections import defaultdict

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted1: List[int]) -> int:
        graph = defaultdict(list)
        restricted = set(restricted1)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        self.count = 0
        visited = set()
        def dfs(root):
            if root in restricted or root in visited:
                return 0
            x = 1
            visited.add(root)
            if root not in graph:
                return x
            for i in graph[root]:
                a = dfs(i)
                x += a
            return x
        return dfs(0)
    
print(Solution().reachableNodes(7, [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], [4,2,1]))