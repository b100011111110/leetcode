from typing import *

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        occupied = [[0]*n for i in range(m)]
        def search(board,cur,i,j):
            if cur == len(word):
                return True
            if 0 <= i < n and 0 <= j < m:
                if occupied[j][i] == 1:
                    return False
                if board[j][i] != word[cur]:
                    return False
            else:
                return False
            occupied[j][i] = 1
            a = search(board,cur+1,i,j-1)
            b = search(board,cur+1,i,j+1)
            c = search(board,cur+1,i-1,j)
            d = search(board,cur+1,i+1,j)
            occupied[j][i] = 0
            return a or b or c or d 
        for i in range(n):
            for j in range(m):
                if board[j][i] == word[0]:
                    x = search(board,0,i,j)
                    if x:
                        return True
        return False