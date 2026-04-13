from collections import deque

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        ans = 0
        que = deque()
        que.append((0,x))
        while que:
            s,n = que.popleft()
            if n == y:
                ans = s
                break
            if n%11 == 0:
                que.append((s+1,n//11))
            if n%5 == 0:
                que.append((s+1,n//5))
            que.append((s+1,n-1))
            que.append((s+1,n+1))
        return ans