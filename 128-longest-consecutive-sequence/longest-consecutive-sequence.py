class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We can think of this problem as trying to find the start of each sequence, then finding the length of the sequence
        # that originates at that starting point, and then getting the max of those lengths. 
        # Use a set, find starts of sequences by checking if i-1 is in the set, then just iterate to count len from that seq.
        # return max
        numSet = set(nums)
        sol = 0
        for i in numSet:
            # we know this is the start of a sequence
            if i-1 not in numSet:
                j = i
                currLen = 0
                # see how long of a consecutive sequence starts at the starting point we found
                while j in numSet:
                    currLen += 1
                    j += 1
                sol = max(sol, currLen)
        
        return sol