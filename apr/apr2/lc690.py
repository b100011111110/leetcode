class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        map = {}
        for i in employees:
            map[i.id] = i
        def dfs(root):
            x = root.importance
            for i in root.subordinates:
                x += dfs(map[i])
            return x
        return dfs(map[id])