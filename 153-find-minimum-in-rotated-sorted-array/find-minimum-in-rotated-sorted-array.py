class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        sol = 5001

        while left <= right:
            mid = (left+right)//2 # average

            sol = min(sol, nums[mid])

            if nums[left] <= nums[mid]:
                sol = min(sol, nums[left])
                left = mid + 1
            elif nums[right] > nums[mid]:
                right = mid - 1
            
        return sol

