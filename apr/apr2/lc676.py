class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class MagicDictionary:
    def __init__(self):
        self.root = TrieNode()
    def buildDict(self, dictionary: list[str]) -> None:
        for word in dictionary:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True

    def search(self, searchWord: str) -> bool:
        def dfs(node, index, modified):
            if index == len(searchWord):
                return modified and node.is_end
            char = searchWord[index]            
            if char in node.children:
                if dfs(node.children[char], index + 1, modified):
                    return True            
            if not modified:
                for next_char in node.children:
                    if next_char != char: 
                        if dfs(node.children[next_char], index + 1, True):
                            return True
            return False

        return dfs(self.root, 0, False)