class Solution:
    def reverseWords(self, s: str) -> str:
        sArr = s.split(" ")
        sol = ""
        for i in sArr:
            i = i[::-1]
            sol += i
            sol += " "
        
        return sol[:len(sol)-1]
            