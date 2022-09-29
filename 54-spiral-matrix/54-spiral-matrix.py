class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        
        left = 0
        right = len(matrix[0]) - 1
        up = 0 
        down = len(matrix) - 1
        
        while left <= right and up <= down:
        
            for i in range(left, right + 1):
                spiral.append(matrix[up][i])
                

            for i in range(up + 1, down + 1):
                spiral.append(matrix[i][right])
            
            if up != down:
                for i in range(right - 1, left - 1, -1):
                    spiral.append(matrix[down][i])
            
            if right != left:
                for i in range(down - 1, up, -1):
                    spiral.append(matrix[i][left])
            
            left += 1
            right -= 1
            up += 1
            down -= 1
        
        return spiral