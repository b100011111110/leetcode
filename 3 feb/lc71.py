from typing import *

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        ans = []
        for i in path:
            if i == '':
                path
            elif i == '..':
                ans.pop()
            else:
                ans.append(i)
        print(ans)
        return '/'.join(ans)

print(Solution().simplifyPath("/home//foo/"))