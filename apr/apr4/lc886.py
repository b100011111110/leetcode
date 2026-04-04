from typing import List
from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        visited,s1,s2 = set(),set(),set()
        graph = defaultdict(list)
        for i,j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        for i,j in dislikes:
            if i not in visited:
                que = deque([[i,True]])
                while que:
                    node,st = que.popleft()
                    if node in visited:
                        if st and node in s2:
                            return False
                        if not st and node in s1:
                            return False
                        continue
                    visited.add(node)
                    if st:
                        s1.add(node)
                    else:
                        s2.add(node)
                    for i in graph[node]:
                        que.append((i,not st))
        return True