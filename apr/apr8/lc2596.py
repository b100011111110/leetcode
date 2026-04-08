from typing import List

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        map = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                map[grid[i][j]] = (i,j)
        for i in range(len(map)-1):
            a = map[i]
            b = map[i+1]
            x,y = abs(a[0]-b[0]),abs(a[1]-b[1])
            if (x,y) not in [(1,2),(2,1)]:
                return False
        return True