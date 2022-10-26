class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        # if it is less than the first element, insert into the beginning of the list
        if newInterval[0] < intervals[0][0]:
            intervals.insert(0, newInterval)
        else:   
            # iterate through the list of intervals, inserting newInterval after the existing interval with
            # a start value that is less than or equal to it
            for i in range(len(intervals)):
                if newInterval[0] >= intervals[i][0]:
                    intervals.insert(i+1, newInterval)
        
        # if there is only one interval, we can just return it
        if len(intervals) == 1:
                return intervals
        
        i = 1
        intervals.sort()
        currMin = intervals[0][0]
        currMax = intervals[0][1]
        returnList = []

        while i < len(intervals):
            # if the next interval does not intersect with our current merge values,
            # add a new interval that is [currMin, currMax] to the new list, 
            # start again at the next interval
            if intervals[i][0] > currMax:
                returnList.append([currMin, currMax])
                currMin = intervals[i][0]
            
            # if the next interval overlaps with our current, we update currMax to be the next intervals max
            if intervals[i][1] > currMax:
                currMax = intervals[i][1]
            i += 1

        returnList.append([currMin, currMax])
        return returnList