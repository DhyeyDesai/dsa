# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        currentStack = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(currentStack))
                return
            
            if openN < n:
                currentStack.append("(")
                backtrack(openN+1, closedN)
                currentStack.pop()
                
            if closedN < openN:
                currentStack.append(")")
                backtrack(openN, closedN+1)
                currentStack.pop()

        
        backtrack(0, 0)
        return result
            