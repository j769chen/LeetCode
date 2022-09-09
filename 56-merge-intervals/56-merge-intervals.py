class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        i = 1
        intervals.sort()
        currMin = intervals[0][0]
        currMax = intervals[0][1]
        returnList = []
    
        while i < len(intervals):
                      
            if intervals[i][0] > currMax:
                returnList.append([currMin, currMax])
                currMin = intervals[i][0]
                
            if intervals[i][1] > currMax:
                currMax = intervals[i][1]
            i += 1
        
        returnList.append([currMin, currMax])
        return returnList