# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/description/

# INTUITION:
# 1. Instead of checking every possible substring (O(n³)), we expand around centers
# 2. Every palindrome has a "center" - either a single character or between two characters
# 3. For each possible center, we expand outward while characters match
# 4. This gives us O(n²) time since we have n centers and each expansion is at most n steps

# KEY INSIGHTS:
# - Odd-length palindromes: center is a single character (i, i)
# - Even-length palindromes: center is between two characters (i, i+1)
# - We need to check both cases for every position to catch all palindromes


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def countPalindromes(s, l, r):
            res = 0
            # Expand around center while characters match and we're in bounds
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1        # Found a palindrome
                l -= 1          # Expand left
                r += 1          # Expand right
            return res

        # Check every possible center position
        for i in range(len(s)):
            # Case 1: Odd-length palindromes centered at position i
            # Example: "aba" centered at middle 'b'
            res += countPalindromes(s, i, i)
            
            # Case 2: Even-length palindromes centered between i and i+1
            # Example: "abba" centered between the two 'b's
            res += countPalindromes(s, i, i + 1)
            
        return res