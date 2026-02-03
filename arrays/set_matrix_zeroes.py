# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstColZero = False
        firstRowZero = False

        # Check if first row has zero
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                firstColZero = True
                break
        
        # Check if first column has zero
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                firstRowZero = True
                break
        
        # Use first row and column as markers
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Zero out cells based on markers
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        # Handle first row
        if firstColZero:
            for row in range(len(matrix)):
                matrix[row][0] = 0

        # Handle first column
        if firstRowZero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0