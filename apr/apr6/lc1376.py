from collections import defaultdict
from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(manager)):
            graph[manager[i]].append(i)
        ans = 0
        def dfs(root,time):
            nonlocal ans
            if root not in graph:
                return 
            time += informTime[root]
            ans = max(ans,time)
            for i in graph[root]:
                dfs(i,time)
        dfs(graph[-1][0],0)
        return ans