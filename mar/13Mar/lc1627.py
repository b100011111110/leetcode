from typing import List
from collections import defaultdict

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        grd = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grd.append((i,j))
        grid = grd
        x,y = defaultdict(list),defaultdict(list)
        visited = set()
        for i in grid:
            x[i[0]].append(i)
            y[i[1]].append(i)
        c = 0
        for i in grid:
            if i not in visited:
                n = 0
                que = [i]
                while que:
                    n += 1
                    node = que.pop(0)
                    visited.add(node)
                    for j in x[node[0]]:
                        if j not in visited:
                            visited.add(j)
                            que.append(j)
                    for j in y[node[1]]:
                        if j not in visited:
                            visited.add(j)
                            que.append(j)
                if n != 1:
                    c += n
        return c