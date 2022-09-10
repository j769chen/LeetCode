class Solution:
    def isPalindrome(self, s: str) -> bool:    
	
        testS = ""
        for i in range(len(s)):
            if s[i].isalnum() is True:
                testS = testS + s[i]

        testS = testS.lower()
        reverseS = testS[::-1]

        if testS == reverseS:
            return True