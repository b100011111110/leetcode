from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        x = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j in x:
                    x[i+j].append(mat[i][j])
                else:
                    x[i+j] = [mat[i][j]]
        p = False
        ans = []
        for i in x:
            if p:
                ans.extend(x[i])
            else:
                ans.extend(x[i][::-1])
            p = not p
        return ans
