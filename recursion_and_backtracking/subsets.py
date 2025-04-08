# 78. Subsets
# https://leetcode.com/problems/subsets/description/


# 1. Iterative Approach


# Intuition:
# - Start with an empty subset.
# - For every number in nums:
#     → Take all existing subsets.
#     → For each subset, create a new subset by adding the current number.
#     → Add all these new subsets to the result.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Start with the empty subset
        result = [[]]

        # Iterate through each number in nums
        for num in nums:
            # For every existing subset in result,
            # create a new subset that includes the current number
            newSubsets = []

            for subset in result:
                newSubsets.append(subset + [num])
            
            # Add all newly created subsets to the result
            result.extend(newSubsets)
        
        return result

# 2. Recursive Approach - Backtracking

# Intuition:
# - At every index, we have 2 choices:
#   1. Include the current element in the subset.
#   2. Exclude the current element from the subset.
# - We explore both choices using DFS (Depth First Search).
# - Once we reach the end of the array (base case), we add the current subset to the result.


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        # Recursive DFS function to explore all possible subsets (Build a decision tree)
        def dfs(i):
            # Base case: If we have considered all elements,
            # add the current subset to the result
            if i>=len(nums):
                result.append(subset.copy())
                return
            
            # Choice 1: Include nums[i] in the current subset
            subset.append(nums[i])
            dfs(i+1)

            # Choice 2:  Backtrack - Remove nums[i] and explore without it
            subset.pop()
            dfs(i+1)
        
        # Start DFS from index 0.
        dfs(0)
        
        return result
