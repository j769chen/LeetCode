class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()
        
        def backtrack(r):
            # if we get past the last row, we have found a solution so we create a copy 
            # and append to result
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                
                board[r][c] = "Q"
                
                backtrack(r+1)
                
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                
                board[r][c] = "."
        
        res = []
        board = [["."] * n for i in range(n)]
        
        backtrack(0)
        
        return res