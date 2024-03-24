class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        t = set()
        for i in nums:
            if i in t:
                return True
            t.add(i)
        return False