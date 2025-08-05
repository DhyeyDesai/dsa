# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/description/

# Intuition
# Our approach uses depth-first search with backtracking:
# - Sort candidates to enable early termination when we exceed the target
# - For each element, we either include it in our combination or not
# - If including it keeps us under target, recurse further with this element still available
# - Once we find a valid combination or hit a dead end, backtrack and try another path

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        # Sort the candidates to enable early termination when exceeding target.
        candidates.sort()

        def dfs(startIdx, currentCombo, currentSum):
            # Base case: we've found a valid combination
            if currentSum == target:
                # Create a copy of currentCombo before adding to result
                # as currentCombo will be modified during backtracking
                result.append(currentCombo.copy())
                return 
            
            # Explore candidates starting from startIdx
            # (we can reuse elements, so we don't increment by default)
            for i in range(startIdx, len(candidates)):
                num = candidates[i]

                # Early termination: if current number makes sum exceed target,
                # all subsequent numbers will also exceed (since array is sorted)
                if currentSum + num > target:
                   break
                
                # Recursive case: include current number in the combination
                currentCombo.append(num)

                # Notice we pass i (not i+1) to allow reusing the same element
                dfs(i, currentCombo, currentSum+num)
                
                # Backtrack: remove the number to try other combinations
                currentCombo.pop()

        # Start DFS with empty combination and sum 0        
        dfs(0, [], 0)
        return result