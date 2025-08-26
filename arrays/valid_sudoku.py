# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/description/

from collections import defaultdict

# Intuition:
# A valid Sudoku requires each digit 1-9 to appear at most once in each row, column, 
# and 3x3 sub-box. We use three hash sets to track seen numbers for each row, column, 
# and box. For any non-empty cell, we check if its digit already exists in the 
# corresponding row, column, or box. If so, it's invalid. Otherwise, we add it to 
# all three sets and continue. The key insight is using (r//3, c//3) to map any 
# cell to its 3x3 box identifier.

# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to track seen digits in each row, column, and 3x3 box
        cols = defaultdict(set)  # cols[c] = set of digits seen in column c
        rows = defaultdict(set)  # rows[r] = set of digits seen in row r
        boxes = defaultdict(set) # boxes[(r//3,c//3)] = set of digits seen in that 3x3 box

        # Iterate through every cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                # Skip empty cells
                if board[r][c] == ".":
                    continue
                
                # Check if current digit violates Sudoku rules
                # It's invalid if the digit already exists in the same row, column, or box
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in boxes[(r//3, c//3)]):
                    return False
                
                # Add the digit to the corresponding row, column, and box sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                # Map cell (r,c) to its 3x3 box using integer division
                # Box (0,0) contains cells [0-2][0-2], box (0,1) contains [0-2][3-5], etc.
                boxes[(r//3, c//3)].add(board[r][c])
        
        # If we've checked all cells without finding violations, the board is valid
        return True

