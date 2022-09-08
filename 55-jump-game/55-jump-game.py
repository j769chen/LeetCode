class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0;
        
        if len(nums) == 1:
            return True
        
        for i in range(len(nums)-1):
            currReach = i + nums[i]
            
            if currReach > maxReach:
                maxReach = currReach
                
            if maxReach <= i:
                return False
        
        return True