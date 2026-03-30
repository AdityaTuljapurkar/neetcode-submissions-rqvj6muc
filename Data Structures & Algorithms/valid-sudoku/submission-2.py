class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        square = {}
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                form = ((r//3)*3)+(c//3)
                if r not in row:
                    row[r] = set()
                if c not in col:
                    col[c] = set()
                if form not in square:
                    square[form] = set()

                if board[r][c].isdigit():    
                    if board[r][c] in row[r] or  board[r][c] in col[c] or board[r][c] in square[form] :
                        return False 
                    else:
                        row[r].add(board[r][c])
                        col[c].add(board[r][c]) 
                        square[form].add(board[r][c])
                else : continue 

        return True         
                

        