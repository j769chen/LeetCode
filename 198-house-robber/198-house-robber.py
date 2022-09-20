class Solution:
    def rob(self, nums: List[int]) -> int:
        firstPrev, secondPrev = 0, 0
        
        for i in nums:
            curr = max(i + secondPrev, firstPrev)
            secondPrev = firstPrev
            firstPrev = curr
        
        return curr
            