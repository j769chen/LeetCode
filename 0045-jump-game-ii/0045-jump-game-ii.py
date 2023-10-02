class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # x represents the max reachable idx from the curr idx
        x = []
        for i in range(len(nums)):
            x.append(i + nums[i])
        
        l,r,jumps = 0,0,0

        while r < len(nums) - 1:
            jumps += 1
            temp = r
            r = max(x[l:r+1])
            l = temp + 1
            
        
        return jumps

        