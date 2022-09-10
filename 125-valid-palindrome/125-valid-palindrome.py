class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ''.join(ch for ch in s if ch.isalnum())
        
        newString = newString.lower() 

        for i in range(0, len(newString)//2):
            if newString[i] != newString[len(newString) - i - 1]:
                return False
        
        return True