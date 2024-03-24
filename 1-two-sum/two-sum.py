class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        imap = {}

        for i in range(len(nums)):
            if target - nums[i] in imap:
                return [i, imap[target - nums[i]]]
            imap[nums[i]] = i