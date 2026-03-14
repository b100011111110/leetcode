class Solution:
    def numDecodings(self, s: str) -> int:
        visited = {}
        def traverse(i):
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            if i in visited:
                return visited[i]
            if s[i] == '0':
                return 0
            elif s[i] == '1':
                if i != len(s)-1:
                    if s[i+1] != '0':
                        x = traverse(i+1) + traverse(i+2)
                    else:
                        x = traverse(i+2)
                else:
                    x = traverse(i+1)
                visited[i] = x
                return x
            elif s[i] == '2':
                if i != len(s)-1:
                    if '0'<=s[i+1]<='6':
                        if s[i+1] != '0':
                            x = traverse(i+1) + traverse(i+2)
                        else:
                            x = traverse(i+2)
                    else:
                        x =  traverse(i+1)
                else:
                    x = traverse(i+1)
                visited[i] = x
                return x
            x = traverse(i+1)
            visited[i] = x
            return x
        if s[0] == '0':
            return 0
        return traverse(0)