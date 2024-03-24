class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while True:
            currSum = numbers[left] + numbers[right]
            if  currSum == target:
                return [left + 1, right + 1]
            elif currSum > target:
                right = right - 1
            else:
                left = left + 1