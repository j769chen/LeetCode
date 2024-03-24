class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t != '+' and t != '-' and t != '*' and t != '/':
                stack.append(int(t))
            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if t == '+':
                    stack.append(num2 + num1)
                elif t == '-':
                    stack.append(num2 - num1)
                elif t == '*':
                    stack.append(num2 * num1)
                elif t == "/":
                    raw = num2 / num1
                    if raw < 0:
                        stack.append(ceil(raw))
                    else:
                        stack.append(floor(raw))
                
        return stack[-1]        