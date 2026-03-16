from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
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
        a = 0
        for i in range(n):
            if grid[i][0] == 1:
                a += dfs(i,0)
            if grid[i][m-1] ==1:
                a += dfs(i,m-1)
        for j in range(m):
            if grid[0][j] == 1:
                a += dfs(0,j)
            if grid[n-1][j] ==1:
                a += dfs(n-1,j)
        c = 0
        for i in range(n):
            for j in range(m):
                c += grid[i][j]
        return c-a