class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        
        while l != r:
            area = max(min(height[r], height[l]) * (r - l), area)
            
            if height[r] < height[l]:
                r = r - 1
            elif height[l] <= height[r]:
                l = l + 1
        
        return area
            
            
            