class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiag = set() # r - c
        negDiag = set() # r + c
        
        sol = 0
        
        def nQueensRecurs(r: int, n: int) -> int:
            # we've filled out every row, so we know that 
            # this is a possible solution
            if r == n:
                nonlocal sol 
                sol += 1
                return 
            
            # iterate through each col
            for c in range(n):
                if c in cols or (r-c) in posDiag or (r+c) in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add(r-c)
                negDiag.add(r+c)
                
                nQueensRecurs(r+1, n)
                
                cols.remove(c)
                posDiag.remove(r-c)
                negDiag.remove(r+c)
            
            
        nQueensRecurs(0, n)
        
        return sol