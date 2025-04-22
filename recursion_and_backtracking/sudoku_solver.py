# 37. Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/

# Solution 1 - Iteration with Backtracking

# Intuition:
# Sudoku solving is a classic backtracking problem where we:
# 1. Find an empty cell
# 2. Try placing each digit (1-9) in that cell
# 3. Check if the placement is valid according to Sudoku rules (row, column, 3x3 box)
# 4. If valid, recursively attempt to solve the rest of the board
# 5. If we reach a dead end, backtrack by removing the last placement and try the next digit
#
# The solution implements a systematic way to try all possible valid configurations
# until we find one that completes the puzzle.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        def backtrack():
            # Start iterating for each cell in the board.
            for row in range(9):
                for col in range(9):
                    # Find an empty cell (marked with '.')
                    # Try placing digits 1-9 in this empty cell
                    if board[row][col] == '.':
                        for digit in '123456789': 
                            # If placing this digit is valid
                            if isValid(row, col, digit):
                                # Place the digit and attempt to solve the rest
                                board[row][col] = digit

                                # Recursively try to solve the rest of the puzzle
                                if backtrack():
                                    return True
                                
                                # If we couldn't solve with this digit, backtrack
                                board[row][col] = '.'

                        # If we tried all digits and none worked, this path fails
                        return False

            # If there are no empty cells left, we solved the puzzle
            return True
        
        # Checks if placing 'digit' at board[row][col] is valid according to Sudoku rules
        def isValid(row, col, digit):
            
            # Check if this digit occurs in the same row or the same column.
            for i in range(9):
                if board[row][i] == digit or board[i][col] == digit:
                    return False
            
            # Check 3x3 sub-box constraint
            boxRowStart = (row//3)*3
            boxColStart = (col//3)*3

            for boxRow in range(boxRowStart, boxRowStart+3):
                for boxCol in range(boxColStart, boxColStart+3):
                    currentValue = board[boxRow][boxCol]
                    if currentValue == digit:
                        return False
            
            # If we reach here, the placement is valid            
            return True
        
        # Call backtrack
        backtrack()

            
        
        