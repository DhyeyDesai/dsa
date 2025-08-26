# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/


# Intuition:
# The key insight is to use a set for O(1) lookups and only start counting sequences 
# from their beginning elements. For each number, we check if it's the start of a 
# sequence (i.e., num-1 doesn't exist in the set). If it is, we count how long the 
# consecutive sequence extends from that starting point. This ensures each number 
# is only processed once as part of exactly one sequence, giving us O(n) time complexity.


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert to set for O(1) lookup time and remove duplicates
        numSet = set(nums)
        longestSequence = 1
        
        # Iterate through each unique number
        for num in numSet:
            # Only start counting if this is the beginning of a sequence
            # (i.e., num-1 doesn't exist in the set)            
            if num - 1 not in numSet:
                length = 1 # Current sequence length starts at 1

                # Keep extending the sequence while consecutive numbers exist            
                while num+length in numSet:
                    length+=1
                
                # Update the maximum sequence length found so far
                longestSequence = max(length, longestSequence)

        return longestSequence