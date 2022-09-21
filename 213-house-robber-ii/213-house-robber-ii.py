class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.robHelper(nums[1:]), self.robHelper(nums[:-1]))
    
    def robHelper(self, nums: List[int]) -> int:
        firstPrev, secondPrev = 0, 0
        
        for i in nums:
            curr = max(i + secondPrev, firstPrev)
            secondPrev = firstPrev
            firstPrev = curr
        
        return curr