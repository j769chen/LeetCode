class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        smap = {}
        sol = []
        for s in strs:
            temp = ''.join(sorted(s))
            if temp in smap:
                smap[temp].append(s)
            else:
                smap[temp] = [s]
        
        for arr in smap.values():
            sol.append(arr)
        
        return sol
