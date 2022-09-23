class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for j in range(n)] for i in range(m)]
        
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 or j == n-1:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i+1][j] + grid[i][j+1]
        
        print(grid)
        return grid[0][0]