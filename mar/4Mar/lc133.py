from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        if node.neighbors == None:
            return node
        x = {}
        visited = set()
        def dfs1(node):
            if node in x:
                return
            x[node] = Node(node.val)
            for i in node.neighbors:
                dfs1(i)
        def dfs2(node):
            if node in visited:
                return
            visited.add(node)
            for i in node.neighbors:
                x[node].neighbors.append(x[i])
            for i in node.neighbors:
                dfs2(i)
        dfs1(node)
        dfs2(node)
        return x[node]