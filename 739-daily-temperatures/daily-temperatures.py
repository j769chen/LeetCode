class Solution:
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # declare an empty stack and a solution arr thats the length of the og arr but all 0s
        # iterate through array by idx, while stack not empty and the top elt of stack is less than 
        # temp at curr idx, pop it, solution at that idx is curr idx - temp_idx
        # append the curr idx to the stack
        stack = []
        sol = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                temp_index = stack.pop()
                sol[temp_index] = i - temp_index
            stack.append(i)
        
        return sol