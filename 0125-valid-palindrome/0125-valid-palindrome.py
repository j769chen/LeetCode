class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s1="".join(c.lower() for c in s if c.isalnum())

        for i in range(len(s1)/2):
            if s1[i] != s1[len(s1)-1-i]:
                return False
        
        return True