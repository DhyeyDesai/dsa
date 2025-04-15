# 46. Permutations
# https://leetcode.com/problems/permutations/description/


# Solution 1: Backtracking using DFS
# Intuition:
# To generate all permutations, for each position in the permutation, 
# we try every unused number. Once a number is used, we mark it unavailable 
# for the current path. After exploring a path, we backtrack (undo the choice)
# and try other possibilities. This gives us all possible n! permutations.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(current, choices,  pickIt):
           # Base case: If the current permutation has all elements,
            # add it to the result list.
            if len(current) == len(choices):
                res.append(current[:])  # Make a copy since current changes later
                return
            
            # Explore all available choices for the next position
            for j in range(len(choices)):
                if pickIt[j] == True:

                    # Choose element choices[j] and mark it as used
                    current.append(choices[j])
                    pickIt[j] = False

                    # Explore further with the current choice
                    backtrack(current, choices, pickIt)

                    # Backtrack: Undo the choice for the next iteration
                    current.pop()
                    pickIt[j] = True

        # Initialize all numbers as available to pick
        pickIt = [True] * len(nums)

        # Start backtracking with an empty permutation
        backtrack([], nums, pickIt)
        return res
    


# Solution 2: Backtracking (Optimal)

# Intuition:
# Instead of using extra space to track used elements, 
# we can generate permutations by swapping elements in-place.
# Idea → Fix one position at a time:
# - Start from index idx and try placing every possible number at that position.
# - Swap the chosen element to idx and recursively permute the rest.
# - After recursion, swap back (backtrack) to restore the original state.
# This avoids using extra space for a 'visited' array, making it more optimal in terms of space.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], idx: int):
        # Base case: All positions are filled → Add current permutation
        if idx == len(nums):
            self.res.append(nums[:])  # Append a copy since nums will change
            return

        # Explore all choices for the current position idx
        for i in range(idx, len(nums)):
            # Choose nums[i] for position idx by swapping
            nums[idx], nums[i] = nums[i], nums[idx]

            # Recurse to fill the next position
            self.backtrack(nums, idx + 1)
            
            # Backtrack: Undo the swap to try another choice
            nums[idx], nums[i] = nums[i], nums[idx]