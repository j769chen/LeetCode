class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        
        grid = [[0 for j in range(n)] for i in range(m)]
        
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (obstacleGrid[i][j] == 1):
                    grid[i][j] = 0
                elif i == m-1 and j == n-1:
                    grid[i][j] = 1
                elif i == m-1:
                    grid[i][j] += grid[i][j+1]
                elif j == n-1:
                     grid[i][j] += grid[i+1][j]
                else:
                    grid[i][j] = grid[i+1][j] + grid[i][j+1]
        

        return grid[0][0]