class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def compareMaps(chars: {}, expectedChars: {}) -> bool:
            for k in chars.keys():
                if chars[k] < expectedChars[k]:
                    return False
            return True
                    
        smallestLength = len(s) + 1
        left, right = 0, 0
        smallestLeft, smallestRight = 0, 0
        expectedChars = {}
        chars = {}
        
        # initialize tracking hashmap occurences to 0
        # and expected hashmap to correct values
        for c in t:
            chars[c] = 0
            
            if c in expectedChars:
                expectedChars[c] = expectedChars[c] + 1
            else:
                expectedChars[c] = 1
        
        substr = s[0]
        
        
        while right < len(s):
            # If the rightmost character that we've seen is a character in 't', we update the 
            # occurence map
            if s[right] in chars.keys():
                chars[s[right]] = chars[s[right]] + 1
            
            # check if we have 't' in our current substring
            tFound = compareMaps(chars, expectedChars)       
            
            if tFound:
                while tFound:
                    # check if the length of the current substring is less than the current smallest we've seen
                    # that contains 't'
                    if (right - left) < smallestLength:
                        smallestLength = right - left
                        smallestLeft = left
                        smallestRight = right
                        
                    # if we have it, remove the leftmost character from substring until we do not have
                    # 't' in our substring anymore
                    if s[left] in chars.keys():
                        chars[s[left]] = chars[s[left]] - 1
                        if chars[s[left]] < expectedChars[s[left]]:
                            tFound = False
                    
                    left = left + 1
                    
            
            right = right + 1
   
        if smallestLength > len(s):
         return ""
        
        return s[smallestLeft:smallestRight+1]