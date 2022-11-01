class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        """
        // find start(s)
        // linear scan through 2d array
          // store [x,y] pairs
        // foreach [x,y] pair,  dfs (curr, visited, string[1:])

        """
        # find start letters, do dfs on each start letter, check each adjacent element that isnt visited or out of bounds
        # when we try to go back from a path, we remove the current element from the path (line 26)
        # we check if all of the letters in the word are in the board in order to avoid unecessary searches
        def dfs(curr, visited, word):
            i = curr[0]
            j = curr[1]
            if not word:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j] or curr in visited:
                return False
            visited.add(curr)
            found = dfs((i+1, j), visited, word[1:]) or dfs((i-1, j), visited, word[1:]) or dfs((i, j+1), visited, word[1:]) or dfs((i, j-1), visited, word[1:])
            visited.remove(curr)
            return found 
        
        
        # find possible starting points
        starts = []
        charsInBoard = {}

            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in charsInBoard:
                    charsInBoard[board[i][j]] += 1
                else:
                    charsInBoard[board[i][j]] = 1
                if board[i][j] == word[0]:
                    starts.append((i,j))
                    
        for char in word:
            if char not in charsInBoard:
                return False

        for i in range(len(starts)):
            visited = set()
            if dfs(starts[i], visited, word):
                return True
        return False