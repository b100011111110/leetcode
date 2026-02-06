from typing import *

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m = len(obstacleGrid),len(obstacleGrid[0])
        mat = [[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    mat[i][j] = 0
                elif i == 0 and j == 0:
                    mat[i][j] = 1
                elif i == 0:
                    mat[i][j] = mat[i][j-1]
                elif j == 0:
                    mat[i][j] = mat[i-1][j]
                else:
                    mat[i][j] = mat[i][j-1] + mat[i-1][j]
        return mat[n-1][m-1]