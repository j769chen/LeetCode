class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        curr, prev = len(nums) - 2, len(nums) - 1
        
        while nums[curr] >= nums[prev]:
            curr -= 1
            prev -= 1
            
            #if both pointers run off the end, return
            if prev < 0:
                return
        
        # First time we encounter a decrease, sort everything that happens to the right of curr
        nums[curr+1:] = sorted(nums[curr+1:])
        
        # find the smallest element that is larger than curr and swap
        for i in range(curr+1, len(nums)):
            if nums[i] > nums[curr]:   
                temp = nums[curr]
                nums[curr] = nums[i]
                nums[i] = temp
                break
            