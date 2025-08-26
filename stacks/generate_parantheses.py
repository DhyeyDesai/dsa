# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/


# Intuition:
# We need all valid combinations of n pairs of parentheses.
# This is a backtracking problem: at each step, we can add "(" if we still have opens left,
# or ")" if it would not exceed the number of "(" used. 
# The recursion explores all valid sequences.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []         # Stores all valid combinations
        currentStack = []   # Current sequence being built

        def backtrack(openN, closedN):
            # If both open and close counts reach n, we have a valid sequence
            if openN == closedN == n:
                result.append("".join(currentStack))
                return
            
            # If we can still add an open parenthesis, do so
            if openN < n:
                currentStack.append("(")
                backtrack(openN + 1, closedN)
                currentStack.pop()  # Backtrack (undo choice)
                
            # If we can add a close parenthesis (only if open > closed)
            if closedN < openN:
                currentStack.append(")")
                backtrack(openN, closedN + 1)
                currentStack.pop()  # Backtrack (undo choice)

        # Start recursion with 0 open and 0 close
        backtrack(0, 0)
        return result
