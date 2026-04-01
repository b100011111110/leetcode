from typing import List
from collections import deque,defaultdict

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        visited,ans,map = set(),0,defaultdict(list)
        for i,j in edges:
            map[min(i,j)].append(max(i,j))
        for i in range(n):
            if i not in visited:
                pn = len(visited)
                que = deque([i])
                while que:
                    node = que.pop()
                    if node in visited:
                        continue
                    visited.add(node)
                    que.extend(map[node])
                m = len(visited)-pn
                ans += m*(m-1)//2
        return n*(n-1)//2-ans