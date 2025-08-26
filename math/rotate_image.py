# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/description/

"""
Intuition:
To rotate a matrix 90° clockwise, we can break it down into two simple operations:
1. Reverse the matrix vertically (flip upside down)
2. Transpose the matrix (swap elements across the main diagonal)

Mathematical insight:
- Original position (i, j) should end up at position (j, n-1-i) after 90° clockwise rotation
- Vertical reverse: (i, j) → (n-1-i, j)  
- Transpose: (n-1-i, j) → (j, n-1-i) ✓

This two-step approach is much simpler than trying to rotate elements directly
and avoids the complexity of handling multiple rings or quadrants.
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # Step 1: Reverse the matrix vertically (flip rows upside down)
        # This moves the last row to first, second-last to second, etc.
        # Example: [[1,2,3], [4,5,6], [7,8,9]] → [[7,8,9], [4,5,6], [1,2,3]]
        matrix.reverse()

        # Step 2: Transpose the matrix (swap elements across main diagonal)
        # For each element at position (i,j), swap it with element at (j,i)
        # We only iterate upper triangle (j >= i) to avoid double-swapping
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):  # Start from i to avoid double swap
                # Swap matrix[i][j] with matrix[j][i]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Result: Matrix is now rotated 90° clockwise
        # Example final result: [[7,4,1], [8,5,2], [9,6,3]]