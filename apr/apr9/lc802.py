from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        isTerminal = [False]*len(graph)
        visited = set()
        def dfs(root):
            if graph[root] == []:
                isTerminal[root] = True
                return True
            if root in visited:
                return isTerminal[root]
            visited.add(root)
            x = True
            for i in graph[root]:
                x = x and dfs(i)
            isTerminal[root] = x
            return x
        for i in range(len(isTerminal)):
            if isTerminal[i] == False:
                dfs(i)
        ans = []
        for i in range(len(isTerminal)):
            if isTerminal[i] == True:
                ans.append(i)
        return ans