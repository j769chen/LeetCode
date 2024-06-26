class Solution:
    def trap(self, height: List[int]) -> int:
        # three arrays, max to the left for elt at idx i, 
        # max to the right of elt at idx i, 
        # and one with the min of these values for idx i
        # the amt of water that can be stored at any given idx is min(maxLeftArr[i], maxRightArr[i]) - height[i]
        # discard any numbers that are <= 1 when summing
        maxLeft, maxRight = 0,0
        maxLeftArr = [0] * len(height)
        maxRightArr = [0] * len(height)
        minH = [0] * len(height)

        sol = 0

        for i in range(1, len(height)):
            if height[i-1] > maxLeft:
                maxLeft = height[i-1]
            maxLeftArr[i] = maxLeft
        
        for i in range(len(height) - 2, 0, -1):
            if height[i+1] > maxRight:
                maxRight = height[i+1]
            maxRightArr[i] = maxRight
            
        for i in range(1, len(height)-1):
            minH[i] = min(maxLeftArr[i], maxRightArr[i])
        
        for i in range(0, len(height)):
            temp = minH[i] - height[i]
            if temp > 0:
                sol += temp
        
        return sol
        
