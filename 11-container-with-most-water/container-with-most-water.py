class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        sol = 0

        while left != right:
            sol = max(sol, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        
        return sol
            