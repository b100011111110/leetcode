from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        time = [[float('inf')] * m for i in range(n)]
        visited = []
        def bfs(i,j):
            que = [(i,j,0)]
            while que:
                x,y,c = que.pop(0)
                if not(0<=x<n and 0<=y<m):
                    continue
                if visited[x][y] == 1:
                    continue
                if grid[x][y] == 0 or (grid[x][y] == 2 and c != 0):
                    continue
                grid[x][y] = 3
                visited[x][y] = 1
                time[x][y] = min(time[x][y],c)
                que.extend([(x+1,y,c+1),(x-1,y,c+1),(x,y+1,c+1),(x,y-1,c+1)])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    visited = [[0] * m for i in range(n)]
                    bfs(i,j)
        mx = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 :
                    return -1
                if time[i][j] != float('inf'):
                    mx = max(mx,time[i][j])
        return mx