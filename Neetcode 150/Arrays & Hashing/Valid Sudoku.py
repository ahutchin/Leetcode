from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Number checking sets
        validRows = [set() for _ in range(9)]
        validColumns = [set() for _ in range(9)]
        validSquares = [set() for _ in range(9)]

        # traverse
        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if val == '.': continue
                square = (row // 3) * 3 + (col // 3)
                if (val in validRows[row]) or (val in validColumns[col]) or (val in validSquares[square]):
                    return False
                
                validRows[row].add(val)
                validColumns[col].add(val)
                validSquares[square].add(val)
        
        # return
        return True
                


# Initial Thoughts:
# Some sort of data storing for each row, each column, and each square, that identifies which numbers are already in
# columns, rows, boxes: set() -> that lists numbers that have already shown up
# read one square at a time, checking if num is present in any of those 3 sets

# Option 1: List comprehension (recommended)
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
test = Solution()
print(test.isValidSudoku(board=board))

# for row in range(9):
#     for col in range(9):
#         val = row * col
#         board[row][col] = val

# for row in board:
#     print(row)
    
