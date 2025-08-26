# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/description/

# Method 1: Binary Search - Find the correct row first, then the element.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS-1

        while top <= bot:
            mid = (top + bot)//2
            row  = matrix[mid]
            if target<row[0]:
                bot=mid-1
            elif target>row[-1]:
                top = mid+1
            else:
                break

        if not (top<=bot):
            return False
        
        left, right = 0, COLS-1
        row = (top+bot)//2
        while left<=right:
            mid = (left+right)//2
            num = matrix[row][mid]
            if target<num:
                right =  mid-1
            elif target>num:
                left = mid+1
            else:
                return True
        
        return False
    
# Method 2: One-pass Binary Search
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        left = 0 
        right = ROWS*COLS - 1

        while left <= right:
            mid = left + (right-left)//2
            row = mid//COLS
            col = mid%COLS
            midElement = matrix[row][col]

            if target<midElement:
                right = mid-1
            elif target>midElement:
                left = mid+1
            else:
                return True
            
        return False