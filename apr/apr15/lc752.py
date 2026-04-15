from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def oneUp(num):
            nn = []
            for i in range(len(num)):
                l = num[:i]
                c = str((int(num[i])+1)%10)
                d = str((int(num[i])-1+10)%10)
                r = num[i+1:]
                nn.append(l+c+r)
                nn.append(l+d+r)
            return nn
        que = deque()
        que.append((0,"0000"))
        visited = set()
        while que:
            i,n = que.popleft()
            if n in deadends:
                continue
            if n == target:
                return i
            for j in oneUp(n):
                if j not in deadends and j not in visited:
                    visited.add(j)
                    que.append((i+1,j))
        return -1
    
print(Solution().openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))