class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        
        for n in nums:
            numSet.add(n)
          
        largestStreak, currentStreak = 0, 0
        currentNum = 0
        
        for num in numSet:
            if not num-1 in numSet:
                currentStreak = 1
                currentNum = num
            
            while currentNum+1 in numSet:
                currentStreak += 1
                currentNum += 1
            
            largestStreak = max(largestStreak, currentStreak)
            
            
        
        return largestStreak