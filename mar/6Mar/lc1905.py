from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n,m = len(grid1),len(grid1[0])
        visited = [[0]*m for _ in range(n)]
        def dfs(i,j):
            if 0<=i<n and 0<=j<m:
                if grid2[i][j] == 0:
                    return True
                if visited[i][j] == 1:
                    return True
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    return False
                visited[i][j] = 1
                a = dfs(i+1,j)
                b = dfs(i-1,j)
                c = dfs(i,j+1)
                d = dfs(i,j-1)
                return a and b and c and d
            else:
                return True
        c = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1 and visited[i][j] == 0:
                    if dfs(i,j):
                        c += 1
        return c