# 51. N-Queens - 2
# https://leetcode.com/problems/n-queens-ii/

# Intuition:
# The N-Queens problem asks us to place N queens on an N×N chessboard so that no two queens attack each other.
# A queen can attack horizontally, vertically, and diagonally.
# To solve this:
# 1. We place queens row by row (ensuring only one queen per row)
# 2. For each queen we place, we check if it's safe from attack by previously placed queens
# 3. We use sets to efficiently track occupied columns and diagonals
# 4. We use backtracking to try different possibilities until we find the number of valid solutions

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        # Create an empty board with '.' in each cell
        # Using list comprehension to ensure each row is independent
        board = [["."] *n for i in range(n)]

        # Sets to track occupied positions
        cols = set()           # Columns with queens
        posDiagonals = set()   # Positive diagonals (r+c is constant)
        negDiagonals = set()   # Negative diagonals (r-c is constant)

        def backtrack(row):
            # Base case: If we've successfully placed queens in all rows
            if row == n:
                # Convert the board to the required string format and add to results
                copy = ["".join(row) for row in board]
                result.append(copy)
                return 
            
            # Try placing a queen in each column of the current row
            for col in range(n):
                # Skip if placing a queen here would cause an attack
                if col in cols or (row+col)  in posDiagonals or (row-col)  in negDiagonals:
                    continue
                
                # Place the queen and update our tracking sets
                board[row][col] = 'Q'
                cols.add(col)
                posDiagonals.add(row + col)  # Cells sharing same (row+col) are on same positive diagonal
                negDiagonals.add(row - col)  # Cells sharing same (row-col) are on same negative diagonal

                # Recursively try to place queens in the next row
                backtrack(row+1)

                # Backtrack: remove the queen and clear the tracking sets
                board[row][col] = '.'
                cols.remove(col)
                posDiagonals.remove(row+col)
                negDiagonals.remove(row-col)

        # Start the backtracking process from the first row
        backtrack(0)
        return len(result)