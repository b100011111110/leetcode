from collections import defaultdict
from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, ko: int) -> int:
        graph = defaultdict(list)
        for i,j,k in flights:
            graph[i].append((k,j))
        ko += 1
        que = [(0,ko,src)]
        visited = {}                                    
        while que:
            cost,k_left,node = heapq.heappop(que)
            if k_left < 0:
                continue
            if node in visited and visited[node] >= k_left: 
                continue
            visited[node] = k_left
            if node == dst:
                return cost
            for i in graph[node]:
                heapq.heappush(que,(cost+i[0],k_left-1,i[1]))
        return -1