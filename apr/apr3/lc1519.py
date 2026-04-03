from typing import List
from collections import Counter,defaultdict

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = defaultdict(list)
        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
        ans = [0]*n
        visited = set()
        def dfs(root):
            if root in visited:
                return {}
            visited.add(root)
            if root not in tree:
                ans[root] = 1
                return {labels[root]:1}
            y = Counter({labels[root]:1})
            for i in tree[root]:
                y += Counter(dfs(i))
            ans[root] = y[labels[root]]
            return y
        dfs(0)
        return ans