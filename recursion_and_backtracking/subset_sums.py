# Subset Sums
# https://www.geeksforgeeks.org/problems/subset-sums2234/1

class Solution:
    def subsetSums(self, arr):
                res = []
                # Recursive DFS function to explore all possible subsets (Build a decision tree).
                def backtrack(i, sum):
                        # Base case: If we have considered all elements,
                        # append the current sum to the result
                        if i == len(arr):
                                res.append(sum)
                                return 
                        
                        # Choice 1: Include nums[i] in the current running sum.
                        backtrack(i+1, sum+arr[i])

                        # Choice 1: Do not include nums[i] in the current running sum.
                        backtrack(i+1, sum)

                # Start DFS from index 0 and sum 0.
                backtrack(0, 0)

                return res
	
	
