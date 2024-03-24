class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True

        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
                continue
            
            if len(stack) > 0:
                top = stack[-1]
                if (i == ')' and top == '(') or (i == '}' and top == '{') or (i == ']' and top == '['):
                    stack.pop()
                else:
                    return False
            else:
                return False
            
        return len(stack) == 0
                
                