# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/

# APPROACH:
# ---------
# We use Dynamic Programming with a BOTTOM-UP approach (starting from the end).

# Key Insight:
# - For each character pair text1[i] and text2[j], we have two scenarios:
#   1. If characters MATCH: We take this character (count it as 1) and add the 
#      LCS of the remaining strings (i+1, j+1)
#   2. If characters DON'T MATCH: We take the maximum of:
#      - Skipping current char in text1 (i+1, j)
#      - Skipping current char in text2 (i, j+1)

# Why build from END to START?
# - When we're at position (i, j), we need to know the results of (i+1, j+1), 
#   (i+1, j), and (i, j+1)
# - Building backwards ensures these values are already computed

# DP Table Meaning:
# - dp[i][j] = LCS length of text1[i:] and text2[j:] (from position i/j to end)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a 2D DP table with extra row and column for base case (empty strings)
        # dp[i][j] represents the LCS length for text1[i:] and text2[j:]
        # The +1 gives us a boundary of zeros (when one string is empty, LCS = 0)
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        
        # Iterate BACKWARDS through both strings (bottom-up DP)
        # Start from the last character and move towards the first
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                
                # CASE 1: Characters match!
                # If current characters are the same, we found a common character
                # LCS = 1 (current match) + LCS of remaining substrings
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                
                # CASE 2: Characters don't match
                # We have two choices - skip character from text1 OR skip from text2
                # Take the maximum of both choices:
                #   - dp[i+1][j]: Skip current char in text1, keep char in text2
                #   - dp[i][j+1]: Keep current char in text1, skip char in text2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        # The answer is at dp[0][0] - LCS of complete text1 and text2
        return dp[0][0]


# OPTIMIZATION INTUITION:
# -----------------------
# The original solution uses O(m * n) space for the entire DP table.
# However, we observe that to compute dp[i][j], we only need:
#   - dp[i+1][j+1] (diagonal-down-right)
#   - dp[i+1][j]   (directly below)
#   - dp[i][j+1]   (directly right)

# This means we only need TWO ROWS at a time:
#   1. Current row (being computed)
#   2. Next row (previously computed)

# SPACE COMPLEXITY: O(min(m, n)) - we use the shorter string for our array
# TIME COMPLEXITY: O(m * n) - still same, just more space efficient
class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # OPTIMIZATION: Make sure text2 is the shorter string
        # This minimizes our space usage to O(min(m, n))
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        # We only need two rows: current and next
        # next_row represents dp[i+1][...] (the row below in original 2D table)
        # curr_row represents dp[i][...] (the row we're computing)
        next_row = [0] * (len(text2) + 1)
        curr_row = [0] * (len(text2) + 1)
        
        # Iterate backwards through text1 (outer loop - rows)
        for i in range(len(text1) - 1, -1, -1):
            
            # Iterate backwards through text2 (inner loop - columns)
            for j in range(len(text2) - 1, -1, -1):
                
                # CASE 1: Characters match
                # Take the diagonal value from next_row (represents dp[i+1][j+1])
                if text1[i] == text2[j]:
                    curr_row[j] = 1 + next_row[j + 1]
                
                # CASE 2: Characters don't match
                # max of:
                #   - next_row[j]: skip char in text1 (dp[i+1][j])
                #   - curr_row[j+1]: skip char in text2 (dp[i][j+1])
                else:
                    curr_row[j] = max(next_row[j], curr_row[j + 1])
            
            # After processing row i, it becomes the "next_row" for row i-1
            # Swap the rows (avoid creating new arrays)
            next_row, curr_row = curr_row, next_row
        
        # After all iterations, next_row contains the final results
        # next_row[0] is equivalent to dp[0][0] in the original solution
        return next_row[0]


"""
VISUAL EXAMPLE: text1 = "ace", text2 = "abcde"

We maintain only 2 arrays instead of full 2D table:

Iteration i=2 (char 'e' in text1):
  next_row = [0, 0, 0, 0, 0, 0]  (boundary - empty string)
  curr_row = [1, 1, 1, 1, 1, 0]  (computed for text1[2:])
  
Iteration i=1 (char 'c' in text1):
  next_row = [1, 1, 1, 1, 1, 0]  (previous curr_row)
  curr_row = [2, 2, 2, 1, 1, 0]  (computed for text1[1:])
  
Iteration i=0 (char 'a' in text1):
  next_row = [2, 2, 2, 1, 1, 0]  (previous curr_row)
  curr_row = [3, 2, 2, 1, 1, 0]  (computed for text1[0:])
  
Answer: next_row[0] = 3
"""

# TODO: Figure out how to use only one array