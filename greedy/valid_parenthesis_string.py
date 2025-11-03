# 678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/

# INTUITION:
# 1. Track a RANGE [leftMin, leftMax] of possible open parentheses at each step
# 2. For '*', treat it optimistically (as ')' or empty) for leftMin, 
#    and pessimistically (as '(') for leftMax to cover all possibilities
# 3. If leftMax < 0, even the best interpretation fails (too many ')')
# 4. If leftMin == 0 at the end, there exists a valid interpretation where all parens balance
        
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0 # Range of possible open parentheses count

        for c in s:
            if c == "(":
                # Definite open paren - increases both min and max
                leftMin = leftMin + 1
                leftMax = leftMax + 1
            elif c == ")":
                # Definite close paren - decreases both min and max
                leftMin = leftMin - 1
                leftMax = leftMax - 1
            else: # c == "*"
                # Wildcard: treat optimistically for min - as ')'
                # and pessimistically for max - as '('. 
                # Both min and max would be unmatched if we treat it as a blank.
                leftMin = leftMin - 1
                leftMax = leftMax + 1
            
            # If even the max (most optimistic) goes negative, 
            # we have too many ')' - impossible to balance
            if leftMax < 0:
                return False
            
            # If min goes negative, reset to 0
            # Meaning: we can use earlier '*' as '(' to balance extra ')'
            if leftMin < 0:
                leftMin = 0
        
        # Valid string must have all open parens closed
        # leftMin == 0 means there exists an interpretation with balanced parens
        return leftMin == 0
