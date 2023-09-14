class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        count = 0
        for i in nums:
            if (target-i) in dic.keys():
                return [dic[target-i], count]
            else:
                dic[i] = count
            count += 1 