class Solution:
    def longestPalindrome(self, s: str) -> str:
        resL, resR = 0, 0
        resLength = 0
        
        for i in range(len(s)):
            # check for odd length palindromes, since center will be made of one palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # if we find a palindrome, check that the length is greater, if it is,
                # set the results
                if (r - l + 1) > resLength:
                    resL = l
                    resR = r
                    resLength = r - l + 1
                r += 1 
                l -= 1
            
            # check for even length palindromes, since center will be made of two
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # if we find a palindrome, check that the length is greater, if it is,
                # set the results
                if (r - l + 1) > resLength:
                    resL = l
                    resR = r
                    resLength = r - l + 1
                r += 1 
                l -= 1
                
        
        return s[resL:resR+1]