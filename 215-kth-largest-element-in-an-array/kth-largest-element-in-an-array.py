class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = []

        for i in nums:
            arr.append(-i)

        heapq.heapify(arr)

        for i in range(k-1):
            heapq.heappop(arr)
        
        return -1*heapq.heappop(arr)
        