from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        x = []
        c = True
        for i in board[::-1]:
            if c:
                x.extend(i)
            else:
                x.extend(i[::-1])
            c = not c
        que,ans = [(0,0)],999999
        visited = set()
        while que:
            node,nt = que.pop(0)
            if node < len(x) and x[node] != -1:
                node = x[node]-1
            if node >= len(x)-1:
                ans = min(ans,nt)
                break
            if node in visited:
                continue
            visited.add(node)
            for i in range(6):
                que.append((node+i+1,nt+1))
        return ans if ans != 999999 else -1
    
print(Solution().snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))