class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]);
        
        merged,s,e = [],0,0;
        for x in range(len(intervals)):
            ss,se=intervals[s];
            es,ee=intervals[e];
            cs,ce=intervals[x];
            
            if cs > ee:
                merged.append([ss,ee]);
                s=e=x;
            elif cs >= ss and ce >= ee:
                e=x;
        
        return merged + [[intervals[s][0], intervals[e][1]]];