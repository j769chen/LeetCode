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
        def dfs(curr, visited, word):
            # print("visited", visited)
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
        charsInBoard = {}

            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in charsInBoard:
                    charsInBoard[board[i][j]] += 1
                else:
                    charsInBoard[board[i][j]] = 1
                # if board[i][j] == word[0]:
                #     starts.append((i,j))
                    
        for char in word:
            if char not in charsInBoard:
                return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                visited = set()
                if dfs((i,j), visited, word):
                    return True
        return False