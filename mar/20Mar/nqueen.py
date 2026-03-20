from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows = set()
        c = set(range(n))
        ans = []
        grid = [['.']*n for i in range(n)]

        def check(i,j):
            for r in range(i):
                for c in range(n):
                    if grid[r][c] == 'Q':
                        if c == j or abs(r - i) == abs(c - j):
                            return False
            return True

        def nQueens(i):
            if i == n:
                return True
            x = sorted(list(c - rows))
            for j in x:
                if check(i,j):
                    grid[i][j] = 'Q'
                    rows.add(j)
                    pp = nQueens(i+1)
                    if i == n-1 and pp == True:
                        x = [''.join(ppp) for ppp in grid]
                        ans.append(x)
                    rows.remove(j)
                    grid[i][j] = '.'

        nQueens(0)
        return list(ans)
    
print(*Solution().solveNQueens(4),sep='\n')