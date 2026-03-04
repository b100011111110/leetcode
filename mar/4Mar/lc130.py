from typing import *
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n,m = len(board),len(board[0])
        visited = [[0]*m for i in range(n)]
        def dfs(i,j):
            if 0<=i<n and 0<=j<m:
                if board[i][j] == 'X':
                    return 
                if visited[i][j] == 1:
                    return 
                visited[i][j] = 1
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j-1)
                dfs(i,j+1)
            else:
                return 
        for i in range(n):
            dfs(i,0)
            dfs(i,m-1)
        for i in range(m):
            dfs(0,i)
            dfs(n-1,i)
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0:
                    board[i][j] = 'X'