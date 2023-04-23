class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)] 
        boxes = [[set() for i in range(3)] for j in range(3)]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    # we basically have a set for each row, column and 3x3 square that keeps track of 
                    # what numbers weve seen in those, if we have a duplicate, the sudoku is invalid
                    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[i//3][j//3]:
                        return False

                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[i//3][j//3].add(board[i][j])

        return True