from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        visited = [[0]*m for i in range(n)]
        def dfs(i,j):
            if 0<= i < n and 0 <= j < m:
                if grid[i][j] == 1:
                    return True
                if visited[i][j] == 1:
                    return True
                visited[i][j] = 1
                a = dfs(i+1,j)
                b = dfs(i-1,j)
                c = dfs(i,j+1)
                d = dfs(i,j-1)
                return a and b and c and d
            else:
                return False
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and visited[i][j] == 0 and dfs(i,j):
                    ans += 1
        return ans