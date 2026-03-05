from typing import *

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        c = 0
        for i in range(len(isConnected)):
            if i not in visited:
                que = [i]
                c += 1
                while que:
                    node = que.pop(0)
                    visited.add(node)
                    for i in range(len(isConnected)):
                        if isConnected[node][i] == 1 and i not in visited:
                            que.append(i)
        return c
        