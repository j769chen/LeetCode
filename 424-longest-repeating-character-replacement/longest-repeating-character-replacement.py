class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxFreq = 0
        sol = 0

        for r in range(len(s)):
            #count.get(s[i], 0) gets the current count of the character s[i] from the count dictionary. 
            #If the character s[i] is not already a key in the dictionary, count.get(s[i], 0) returns 
            #the default value of 0.
            count[s[r]] = 1 + count.get(s[r], 0)
            
            maxFreq = max(maxFreq, count[s[r]])

            if (r-l+1) - maxFreq > k:
                count[s[l]]-=1
                l+=1
                
            sol = max(sol,r-l+1)

        return sol