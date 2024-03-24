class Solution:
    # We sort the list, then iterate through. At each outer iteration, 
    # we perform two sum II on the remainder to the right of our idx
    # however, to avoid duplicates, we skip outer iterations of numbers that are equal.
    # we also have to update one of the pointers if we ever find a solution, and apply the same logic for
    # dealing with duplicates
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currSum = nums[i] + nums[left] + nums[right]

                if currSum > 0:
                    right -= 1
                elif currSum < 0:
                    left += 1
                else:
                    sol.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        
        return sol




