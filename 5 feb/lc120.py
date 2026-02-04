from typing import *

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        mat = [[-1]*(i+1) for i in range(n)]
        def traverse(i,j):
            if i == n:
                return 0
            if mat[i][j] != -1:
                return mat[i][j]
            x = traverse(i+1,j)
            y = traverse(i+1,j+1)
            mat[i][j] = min(x,y)+triangle[i][j]
            return min(x,y)+triangle[i][j]
        x = traverse(0,0)
        return x