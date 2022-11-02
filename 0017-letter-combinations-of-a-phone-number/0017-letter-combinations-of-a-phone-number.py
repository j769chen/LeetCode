class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        numberMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def backtrack(currStr, digits, solution, i):
            if len(currStr) == len(digits):
                solution.append(currStr)
                return
            
            for c in numberMap[digits[i]]:
                backtrack(currStr + c, digits, solution, i+1)
                
                
        solution = []
        currStr = ""
        
        backtrack(currStr, digits, solution, 0)
        
        return solution
        
        