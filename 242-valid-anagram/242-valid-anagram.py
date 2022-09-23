class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}
        
        for c in s:
            if s1.get(c) is None:
                s1[c] = 1
            else:
                s1[c] = s1.get(c) + 1
                
        for c in t:
            if s2.get(c) is None:
                s2[c] = 1
            else:
                s2[c] = s2.get(c) + 1
                
        if len(s1) > len(s2):
            for x in s1.keys():
                if (s1.get(x) != s2.get(x)):
                    return False
        else:
            for x in s2.keys():
                if (s2.get(x) != s1.get(x)):
                    return False
                
        return True
            