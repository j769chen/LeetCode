class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)-1 # goal

        if len(nums) <= 1:
            return True
        curr = n
        for i in range(n-1, -1, -1):
            # print("i:",i)
            if curr-i <= nums[i]: # can reach at i
                if i == 0:
                    return True
                curr = i
        return False
        


