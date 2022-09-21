class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        grid = [[0 for j in range(len(text2))] for i in range(len(text1))]


        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if i-1 < 0 or j-1 < 0:
                        grid[i][j] = 1
                    else: 
                        grid[i][j] = 1 + grid[i-1][j-1]
                else:
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])

        return grid[len(text1)-1][len(text2)-1]