class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                temp_index = stack.pop()
                sol[temp_index] = i - temp_index
            stack.append(i)
        
        return sol

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         stack = []
#         ans = [0] * len(temperatures)
        
#         for i in range(len(temperatures)):
#             while stack and temperatures[stack[-1]] < temperatures[i]:
#                 ind = stack.pop()
#                 ans[ind] = (i - ind)
#             stack.append(i)

#         return ans