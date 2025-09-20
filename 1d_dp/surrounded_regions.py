# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/description/


# INTUITION:
# 1. Instead of finding regions to capture directly, we find regions that CANNOT be captured
# 2. Any 'O' connected to the border cannot be surrounded (since it touches the edge)
# 3. We mark all unsurrounded 'O's as temporary 'T', then flip the rest
# 4. This reverse thinking makes the problem much simpler - we only need to check border cells

# KEY INSIGHT: 
# - Surrounded = NOT connected to any border 'O'
# - So we find all border-connected 'O's first, then capture everything else


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])


        def capture(r, c):
            # Base case: out of bounds or not an 'O' to mark
            if (r<0 or r==ROWS or c<0 or c==COLS or board[r][c] != 'O'):
                return
            
            # Mark this 'O' as temporarily safe (connected to border)
            board[r][c] = 'T'

            # Recursively mark all connected 'O's in 4 directions
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Step 1: Mark all 'O's connected to borders as temporary 'T'
        # Check left and right borders (all rows)
        for c in range(ROWS):
            if board[c][0] == 'O':              
                capture(c, 0)
            if board[c][COLS-1] == 'O':         
                capture(c, COLS-1)

        # Check top and bottom borders (all columns)
        for c in range(COLS):
            if board[0][c] == 'O':              
                capture(0, c)
            if board[ROWS-1][c] == 'O':         
                capture(ROWS-1, c)

        
        # Step 2: Final pass - convert markings to final result
        for r in range(ROWS):
            for c in range(COLS):
                # Was connected to border - restore to 'O'
                if board[r][c] == 'T':          
                    board[r][c] = 'O'
                # Was not connected to border - capture as 'X'
                elif board[r][c] == 'O':        
                    board[r][c] = 'X'