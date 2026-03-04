from typing import *

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(list(range(1,n+1)),key=lambda i:str(i))