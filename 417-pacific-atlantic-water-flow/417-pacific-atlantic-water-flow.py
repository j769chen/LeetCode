class Solution:
    # We run dfs from each cell that borders the atlantic, and then each cell that borders the pacific
    # while looking for higher ground, and mark if cells going inwards are reachable from that ocean
    # we then check if the cell is reachable from both oceans by iterating through both matrices that we recorded
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(grid, i, j, visited):
            # print("i:", i, " j:", j)
            height = grid[i][j]
            
            visited[i][j] = True
            
            if i + 1 < len(grid) and visited[i+1][j] == False and grid[i+1][j] >= height:
                dfs(grid, i+1, j, visited)
            if i - 1 >= 0 and visited[i-1][j] == False and grid[i-1][j] >= height:
                dfs(grid, i-1, j, visited)
            if j + 1 < len(grid[0]) and visited[i][j+1] == False and grid[i][j+1] >= height:
                dfs(grid, i, j+1, visited)
            if j - 1 >= 0 and visited[i][j-1] == False and grid[i][j-1] >= height:
                dfs(grid, i, j-1, visited)
                
    
        atlanticCells = []
        pacificCells = []
        
        m = len(heights)
        n = len(heights[0])
        
        for i in range(m):
            atlanticCells.append((i, n-1))
            pacificCells.append((i, 0))
            
        for j in range(n):
            atlanticCells.append((m-1, j))
            pacificCells.append((0, j))
            
        # print("at:", atlanticCells)
        # print("pc:", pacificCells)

        reachableFromAt =  [[False for i in range(n)] for j in range(m)]
        reachableFromPc =  [[False for i in range(n)] for j in range(m)]
        
        for cell in atlanticCells:
            dfs(heights, cell[0], cell[1], reachableFromAt)
            
        for cell in pacificCells:
            dfs(heights, cell[0], cell[1], reachableFromPc)
            
        # print("at:", reachableFromAt)
        # print("pc:", reachableFromPc)
        result = []
        for i in range(m):
            for j in range(n):
                if reachableFromAt[i][j] and reachableFromPc[i][j]:
                    result.append([i,j])
        
        return result