from collections import defaultdict
from typing import List

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        self.ans = 0
        self.visited = set()
        def dfs(root,parent):
            self.visited.add(root)
            if len(graph[root]) == 1 and parent != -1:
                self.ans += 1
                return 1
            ans = set()
            c = 0
            for i in graph[root]:
                if i not in self.visited:
                    x = dfs(i,root)
                    ans.add(x)
                    c += x
            if len(ans) == 1:
                self.ans += 1
            return c + 1
        dfs(0,-1)
        return self.ans
    
print(Solution().countGoodNodes([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]))