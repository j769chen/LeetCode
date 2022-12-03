class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = deepcopy(matrix)
        
        for i in range (len(dp)-2, -1, -1):
            for j in range(len(dp[i])-2, -1, -1):
                if dp[i][j] == "1":
                    if dp[i][j+1] == "0" or dp[i+1][j] == "0" or dp[i+1][j+1] == "0":
                        continue
                    else:
                        print()
                        dp[i][j] = str(min(int(dp[i][j+1]), int(dp[i+1][j]), int(dp[i+1][j+1])) + 1)
        maxSquare = 0
        for i in range(0, len(dp)):
            for j in range(0, len(dp[i])):
                if int(dp[i][j])**2 > maxSquare:
                    maxSquare = int(dp[i][j])**2
        
        return maxSquare
                    
                    