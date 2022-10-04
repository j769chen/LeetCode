class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid: List[List[str]], startingX, startingY):
            if startingX < 0 or startingY < 0 or startingX >= len(grid) or startingY >= len(grid[0]) or grid[startingX][startingY] != "1":
                return


            grid[startingX][startingY] = "2"
            dfs(grid, startingX+1, startingY)
            dfs(grid, startingX-1, startingY)
            dfs(grid, startingX, startingY+1)
            dfs(grid, startingX, startingY-1)
#             stack = []
            
#             stack.append((startingX, startingY))
            
#             while len(stack) > 0:
#                 curr = stack.pop(0)
#                 print(grid)
#                 print("")
#                 grid[curr[1]][curr[0]] = "2"
                
#                 if curr[1] - 1 > 0 and int(grid[curr[1] - 1][curr[0]]) == 1:
#                     stack.append((curr[1] - 1, curr[0]))
                    
#                 if curr[0] - 1 > 0 and int(grid[curr[1]][curr[0] - 1]) == 1:
#                     stack.append((curr[1], curr[0] - 1))
                    
#                 if curr[1] + 1 < len(grid) and int(grid[curr[1] + 1][curr[0]]) == 1:
#                     stack.append((curr[1] + 1, curr[0]))
                    
#                 if curr[0] + 1 < len(grid[0]) and int(grid[curr[1]][curr[0] + 1]) == 1:
#                     stack.append((curr[1], curr[0] + 1))
            
            
            
        numIslands = 0
        
        for i in range(len(grid)):
            for j in range (len(grid[0])):
                if int(grid[i][j]) == 1:
                    
                    dfs(grid, i, j)
                    numIslands += 1
        
        return numIslands
                
    
    