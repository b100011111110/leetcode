from typing import *

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        visited = [[0]*m for _ in range(n)]
        def dfs(i,j):
            if 0<=i<n and 0<=j<m:
                if grid[i][j] == 0:
                    return 0
                if visited[i][j] == 1:
                    return 0
                visited[i][j] = 1
                a = dfs(i+1,j)
                b = dfs(i-1,j)
                c = dfs(i,j+1)
                d = dfs(i,j-1)
                return 1 + a + b + c + d
            else:
                return 0
        c = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    c = max(c,dfs(i,j))
        return c