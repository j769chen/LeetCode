class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        firstPrev, secondPrev = 1, 0
        
        for i in range(1, n):
            curr = firstPrev + secondPrev
            secondPrev = firstPrev
            firstPrev = curr
        
        return curr