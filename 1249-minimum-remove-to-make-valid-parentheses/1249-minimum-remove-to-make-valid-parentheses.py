class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        
        stringList = list(s)
        
        for i in range(len(stringList)):
            if stringList[i] == '(':
                stack.append(stringList[i])
            if stringList[i] == ')':
                if len(stack) < 1:
                    stringList[i] = ""
                else:
                    stack.pop()
        
        stack = []
        
        for i in range(len(stringList) - 1, -1, -1):
            if stringList[i] == ')':
                stack.append(stringList[i])
            if stringList[i] == '(':
                if len(stack) < 1:
                    stringList[i] = ""
                else:
                    stack.pop()
        
        
        sol = "".join(stringList)
        
        return sol
        
        