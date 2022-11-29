class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        seenSoFar = {}
        
        def recurs(idx, sumSoFar):
            if idx == len(nums):
                if sumSoFar == target:
                    return 1
                return 0
            
            if (idx, sumSoFar) in seenSoFar:
                return seenSoFar[(idx, sumSoFar)]
            
            # print("idx: ", idx)
            # print("sumSoFar: ", sumSoFar)
            
            seenSoFar[(idx, sumSoFar)] = recurs(idx+1, sumSoFar - nums[idx]) + recurs(idx+1, sumSoFar + nums[idx])
            
            return seenSoFar[(idx, sumSoFar)]
        
        return recurs(0, 0)
            