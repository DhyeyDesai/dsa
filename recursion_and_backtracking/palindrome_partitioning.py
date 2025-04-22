# 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/description/

# Intuition:
# The problem asks for all ways to split a string into palindromic substrings.
#
# Key approach:
# - Use backtracking to try different partitioning points
# - At each step, check if the current substring is a palindrome
# - If it's a palindrome, add it to our current partition and solve for the remaining string
# - When we reach the end of the string, we've found a complete valid partitioning
#
# Example with "aab": Try all cuts, keeping only palindromes:
# ["a"|"a"|"b"], ["aa"|"b"] are the valid partitionings

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(startIdx, current):
            # Base case: If we've processed the entire string,
            # we've found a valid partitioning
            if startIdx == len(s):
                res.append(current.copy())
                return
            
            # Try all possible substrings starting from current position
            for endIdx in range(startIdx, len(s)):
                # Check if substring s[start_idx:end_idx+1] is a palindrome
                if self.isPalindrome(s, startIdx, endIdx):
                    # Include this palindrome in our current partition
                    current.append(s[startIdx:endIdx+1])

                    # Recursively partition the remaining string
                    backtrack(endIdx+1, current)

                    # Backtrack: remove the palindrome to try other partitioning options
                    current.pop()
        
        # Start partitioning from the beginning with an empty partition
        backtrack(0, [])
        return res
    
    def isPalindrome(self, s, i, j):
        # Check if s[left:right+1] is a palindrome using two pointers
        while i<j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True
