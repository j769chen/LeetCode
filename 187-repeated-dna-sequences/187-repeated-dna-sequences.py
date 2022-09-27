class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        occurences = {}
        
        sequence = s[0:10]
        
        occurences[sequence] = 1
        
        for i in range(10, len(s)):
            sequence = sequence[1:]
            sequence += s[i]
            
            if sequence in occurences:
                occurences[sequence] = occurences[sequence] + 1
            else:
                occurences[sequence] = 1
        
        arr = []
        
        for k in occurences.keys():
            if occurences[k] > 1:
                arr.append(k)
        
        return arr