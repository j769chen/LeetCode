class Solution:
    # bucket sort, we first get the frequencies of each element, then place them into buckets 
    # based on their frequency. We know that the max number of times an element can be in 
    # in the array is the size of the array, so we need a bucket for 0 -> len(arr) frequencies
    # then we can simply go through the buckets and get the top k
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        
        elts = {}

        for n in nums:
            if n in elts:
                elts[n] += 1
            else:
                elts[n] = 1
        
        buckets = [[] for i in range(len(nums)+1)]
        
        for i in elts.keys():
            buckets[elts[i]].append(i)
        
        kElts = []
        print(buckets)
        for i in range(len(buckets)-1, 0, -1):
            print(buckets[i])
            for j in buckets[i]:
                kElts.append(j)
                if len(kElts) == k:
                    return kElts
                
                