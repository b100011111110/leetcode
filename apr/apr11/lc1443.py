from collections import defaultdict
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = set()
        self.count = 0
        def dfs(root):
            a = False
            if hasApple[root] == True:
                a = True
            if root in visited:
                return 0
            visited.add(root)
            if root not in graph:
                if a:
                    return 2
                else:
                    return 0
            c = 0
            for i in graph[root]:
                x = dfs(i)
                c += x
            if c != 0:
                return c+2
            if a:
                return 2
            return 0
        x = dfs(0)
        if x:
            return x - 2
        return x