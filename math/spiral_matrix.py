# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/

"""
Intuition:
Traverse the matrix in spiral order by maintaining four boundaries: top, bottom, left, right.
Move in the pattern: Right → Down → Left → Up, shrinking boundaries after each direction.

The key insight is to:
1. Process one complete direction at a time
2. Update the corresponding boundary after each direction
3. Check if we still have valid boundaries before continuing
4. Handle edge cases where we might traverse the same row/column twice

The boundary checks (top <= bottom, left <= right) prevent processing the same 
elements twice in cases where the matrix becomes a single row or column.
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Handle edge case: empty matrix
        if not matrix:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        
        # Initialize boundaries for the four sides
        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        result = []

        # Continue until we've visited all elements
        while len(result) < rows * cols:
            # Direction 1: Move RIGHT across the top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Shrink top boundary (we've processed this row)

            # Direction 2: Move DOWN along the right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Shrink right boundary (we've processed this column)

            # Direction 3: Move LEFT across the bottom row (if still valid)
            # Check ensures we don't process the same row twice
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Shrink bottom boundary

            # Direction 4: Move UP along the left column (if still valid)  
            # Check ensures we don't process the same column twice
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Shrink left boundary

        return result