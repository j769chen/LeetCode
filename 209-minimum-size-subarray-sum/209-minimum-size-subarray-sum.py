class Solution:
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        currTotal = 0
        left =0
        right = 0
        length = len(nums)

        while right < len(nums):
            currTotal = currTotal + nums[right]
            while currTotal >= target:
                length = min(length, right - left + 1)
                currTotal = currTotal - nums[left]
                left = left + 1

            right = right + 1
            
        if left == 0 and right == len(nums) and currTotal < target:
            return 0
    
        return length