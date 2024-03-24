class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tmap = {}
        smap = {}

        for c in s:
            if c in smap:
                smap[c] += 1
            else: 
                smap[c] = 1
        
        for c in t:
            if c in tmap:
                tmap[c] += 1
            else: 
                tmap[c] = 1
        
        if (len(tmap.keys()) > len(smap.keys())):
            for k in tmap.keys():
                if k not in smap or tmap[k] != smap[k]:
                    return False
        else:
            for k in smap.keys():
                if k not in tmap or smap[k] != tmap[k]:
                    return False
        
        return True