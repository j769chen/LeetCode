class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxes = [1]*len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    maxes[i] = max(maxes[i], maxes[j] + 1)
        
        return max(maxes)
                
                