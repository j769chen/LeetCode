class Solution:
    # There is one way to get to the first step (climb one)
    # There are two ways to get to the 2nd step (climb two, or climb one & one)
    # For every other position, you can get to it either by taking two steps from the step two steps below
    # or by taking one step from the one directly below.
    # thus, it is the number of ways to get to the step two below plus the number of steps to get to the one
    # directly below
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        prev1, prev2 = 1,2
        curr = 0
        i = 2
        
        while i < n:
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
            i += 1
        
        return curr