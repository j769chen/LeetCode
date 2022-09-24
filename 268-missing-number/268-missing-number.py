class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
 
        summ = 0
        for i in nums:
            summ += i
        
        realSum = 0
        for i in range(0, n):
            realSum += i
        
        return realSum - summ