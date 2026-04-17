from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        queue = []
        answer = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
        if not queue or len(queue) == m * n:
            return -1
        while queue:
            x, y, dist = queue.pop(0)
            answer = max(answer, dist)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 0 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny, dist + 1))
        return answer