from typing import List

class TreeNode:
    def __init__(self,name):
        self.name = name
        self.isAlive = True
        self.children = []

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = None
        self.nodes = {}

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.nodes:
            self.nodes[parentName] = TreeNode(parentName)
            self.root = self.nodes[parentName]
        self.nodes[childName] = TreeNode(childName)
        self.nodes[parentName].children.append(self.nodes[childName])

    def death(self, name: str) -> None:
        self.nodes[name].isAlive = False

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        def dfs(root):
            if root == None:
                return 
            print(root)
            if root.isAlive:
                ans.append(root.name)
            for i in root.children:
                dfs(i)
        dfs(self.root)
        return ans            


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()