class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # two arrays to track each row/column and if there has been a 0 in it, this way
        # we skip some unecessary operations
        rows = [0] * len(matrix)
        columns = [0] * len(matrix[0])
        
        
        for i in range (len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    columns[j] = 1
        
        for i in range (len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i] == 1:
                    for k in range(len(matrix[0])):
                            matrix[i][k] = 0
                if columns[j] == 1:
                    for k in range(len(matrix)):
                            matrix[k][j] = 0
        
                