from    typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [0]*(amount+1)
        for i in range(1,amount+1):
            if i in coins:
                arr[i] = 1
            else:
                x = 99999999
                for j in coins:
                    if i-j < 0 or arr[i-j] == 0:
                        continue
                    x = min(x,arr[i-j])
                arr[i] = 1+x
        if arr[-1] == 99999999 + 1:
            return -1
        return arr[-1]