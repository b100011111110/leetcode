from typing import *

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0  
        r, c = 0, 0
        while head:
            res[r][c] = head.val
            head = head.next
            nr = r + dirs[d][0]
            nc = c + dirs[d][1]            
            if not (0 <= nr < m and 0 <= nc < n and res[nr][nc] == -1):
                d = (d + 1) % 4
                nr = r + dirs[d][0]
                nc = c + dirs[d][1]
            r, c = nr, nc
        return res