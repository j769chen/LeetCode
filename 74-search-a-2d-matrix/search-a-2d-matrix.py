class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = bottom-top//2
            if target <= matrix[mid][-1] and target >= matrix[mid][0]:
                print(matrix[0])
                return self.search(matrix[mid], target)
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                bottom = mid - 1

    # binary search for when we find the right array
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = right-left//2
            if target == nums[mid]:
                return True
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return False