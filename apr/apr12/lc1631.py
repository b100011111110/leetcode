from heapq import heappop,heappush
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        que = [(0,0,0)]
        n,m = len(heights),len(heights[0])
        visited = set()
        mdiff = 0
        while que != []:
            e,x,y = heappop(que)
            if x == n-1 and y == m-1:
                break
            if 0<=x<n and 0<=y<m:
                mdiff = max(e,mdiff)
                visited.add((x,y))
                if x != 0 and (x-1,y) not in visited:
                    heappush(que,((abs(heights[x][y] - heights[x-1][y])),x-1,y))
                if x != n-1 and (x+1,y) not in visited:
                    heappush(que,((abs(heights[x][y] - heights[x+1][y])),x+1,y))
                if y != m-1 and (x,y+1) not in visited:
                    heappush(que,((abs(heights[x][y] - heights[x][y+1])),x,y+1))
                if y != 0 and (x,y-1) not in visited    :
                    heappush(que,((abs(heights[x][y] - heights[x][y-1])),x,y-1))
            else:
                continue
        return mdiff