class Solution:
    def myPow(self, x: float, n: int) -> float:
        if 0 > n:
            x = 1/x
            n = -n
        def traverse(n):
            if n == 0:
                return 1
            if n == 1:
                return x
            p = traverse(n//2)
            if n % 2 == 0:
                return p * p
            return p * p * x 
        return traverse(n)
    
print(Solution().myPow(2,-2))