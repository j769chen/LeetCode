class Solution:
   def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        arr=[intervals[0]]
        for i in intervals:
            a=arr[-1]
            if i[0]<=a[1]:
                arr[-1]=[min(a[0],i[0]),max(a[1],i[1])]
            else:
                arr.append(i)
        return arr