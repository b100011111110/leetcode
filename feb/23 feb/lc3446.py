from collections import defaultdict
class Solution:
    def sortMatrix(self, grid):
        n, m = len(grid), len(grid[0])
        diag_map = defaultdict(list)
        for i in range(n):
            for j in range(m):
                key = i - j
                diag_map[key].append(grid[i][j])
        for key in diag_map:
            if key < 0:
                diag_map[key].sort()  
            else:
                diag_map[key].sort(reverse=True)  
        for i in range(n):
            for j in range(m):
                key = i - j
                grid[i][j] = diag_map[key].pop(0)  
        return grid