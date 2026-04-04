from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, ki: int) -> int:
        graph = defaultdict(list)
        for i,j,k in times:
            graph[i].append((j,k))
        que = [(0,ki)]
        visited = set()
        ans = 0
        while que:
            time,node = heappop(que)
            if node in visited:
                continue
            visited.add(node)       
            ans = max(ans,time)
            for i,t in graph[node]:
                if i not in visited:
                    heappush(que,(time+t,i))
        if len(visited) == n:
            return ans
        return -1