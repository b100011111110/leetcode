from typing import List

class Solution:
    def countBattleships(self, grid: List[List[str]]) -> int:
        n,m = len(grid),len(grid[0])
        visited = [[0]*m for _ in range(n)]
        def dfs(i,j):
            if 0<=i<n and 0<=j<m:
                if grid[i][j] == '.':
                    return
                if visited[i][j] == 1:
                    return 
                visited[i][j] = 1
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
            else:
                return 
        c = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'X' and visited[i][j] == 0:
                    c += 1
                    dfs(i,j)
        return c