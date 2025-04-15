# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/

# Intuition:
# The key difference from Combination Sum I is that:
# 1. Each number can only be used ONCE in each combination
# 2. The input array may contain duplicates, but our result should not
#
# To solve this:
# - Sort the array to group duplicates together and enable pruning
# - Use backtracking with a starting index that increases (i+1) to avoid reusing elements
# - Skip duplicate elements AT THE SAME RECURSION LEVEL to avoid duplicate combinations
# - The elegant trick: skip an element if it equals the previous one (i > startIdx && nums[i] == nums[i-1])
#   This ensures we only use the first occurrence of any value at each decision level

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        # Sort to group duplicates together and enable pruning        
        candidates.sort()
        def dfs(startIdx, currentCombo, currentSum):
            # If we've reached our target sum, we found a valid combination
            if currentSum == target:
                # Create a copy of currentCombo before adding to result
                # as currentCombo will be modified during backtracking
                result.append(currentCombo.copy())
                return
            
            for i in range(startIdx, len(candidates)):
                # DUPLICATE HANDLING: Skip duplicates at the same recursion level
                # If current element equals previous element at this level, skip it
                if i > startIdx and candidates[i] == candidates[i-1]:
                    continue

                # PRUNING: If adding this number exceeds target, all future numbers will also exceed
                # (since array is sorted), so we can break early
                if currentSum + candidates[i] > target:
                    break
                
                # Include current element in our combination
                currentCombo.append(candidates[i])

                # Move to next index (i+1 not i) since we can't reuse the same element
                dfs(i+1, currentCombo, currentSum+candidates[i])

                # Backtrack: remove the element before trying next option
                currentCombo.pop()

        # Start DFS with empty combination and sum 0        
        dfs(0, [], 0)
        return result
