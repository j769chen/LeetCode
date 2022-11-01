class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            if not s:
                return True
            else:
                return False
        curMatch = len(s) > 0 and (s[0] == p[0] or p[0] == '.')
        
        if len(p) > 1 and p[1] == '*':
            return curMatch and self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
        return curMatch and self.isMatch(s[1:], p[1:])
            