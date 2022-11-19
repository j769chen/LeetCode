class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slowPointer, fastPointer = 0, 0
        
       
        while True:
            
            slowPointer = nums[slowPointer]
            
            fastPointer = nums[nums[fastPointer]]
            
            if (slowPointer == fastPointer):
                break
        
        
        startPointer = 0
        
        while startPointer != slowPointer:
            startPointer = nums[startPointer]
            
            slowPointer = nums[slowPointer]
            
        print(startPointer)
        
        return startPointer
            
            