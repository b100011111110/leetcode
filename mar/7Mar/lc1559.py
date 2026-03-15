from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n,m = len(grid),len(grid[0])
        visited = [[0]*m for _ in range(n)]
        def dfs(i,j,pi,pj):
            if 0<=i<n and 0<=j<m:
                if grid[i][j] != grid[pi][pj]:       
                    return False
                if visited[i][j] == 1:              
                    return True
                visited[i][j] = 1
                a = dfs(i+1,j,i,j) if not(i+1==pi and j==pj) else False
                b = dfs(i-1,j,i,j) if not(i-1==pi and j==pj) else False
                c = dfs(i,j+1,i,j) if not(i==pi and j+1==pj) else False
                d = dfs(i,j-1,i,j) if not(i==pi and j-1==pj) else False
                return a or b or c or d
            else:
                return False
        c = False
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0:
                    c = dfs(i,j,i,j)            
                    if c:
                        return True
        return False