class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == "":
            return len(word2)
        if word2 == "":
            return len(word1)

        n, m = len(word1), len(word2)
        mat = [[0] * m for _ in range(n)]
        mat[0][0] = 0 if word1[0] == word2[0] else 1

        for i in range(1, n):
            if word1[i] == word2[0]:
                mat[i][0] = min(i, 1 + mat[i-1][0])
            else:
                mat[i][0] = 1 + mat[i-1][0]

        for j in range(1, m):
            if word1[0] == word2[j]:
                mat[0][j] = min(j, 1 + mat[0][j-1])
            else:
                mat[0][j] = 1 + mat[0][j-1]

        for i in range(1, n):
            for j in range(1, m):
                if word1[i] == word2[j]:
                    mat[i][j] = mat[i-1][j-1]
                else:
                    mat[i][j] = 1 + min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1])

        return mat[-1][-1]