# 90. Subsets - 2
# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        # Sort the input array to group duplicates together.
        nums.sort()
        subset = []

        # Recursive DFS function to explore all possible subsets
        def backtrack(i):
            # Base case: If we've considered all elements, add a copy of current subset to result.
            if i == len(nums):
                res.append(subset[:])
                return
            
            # Choice 1: Include nums[i] in the current subset and move to the next element.
            subset.append(nums[i])
            backtrack(i+1)

            # Choice 2: Exclude nums[i] from the current subset (backtrack).
            subset.pop()
            # Skip all consecutive duplicates to avoid generating duplicate subsets.
            while nums[i+1] == nums[i] and i+1<len(nums):
                i +=1
            
            # Move to the next unique element.
            backtrack(i+1)
        
        # Start backtracking from index 0.
        backtrack(0)

        return res
