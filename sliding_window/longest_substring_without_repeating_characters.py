# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Intuition:
# We want the longest substring without repeating characters.
# Use a sliding window: expand with the right pointer, and if a repeat is found,
# move the left pointer to skip past the last occurrence of that character.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}   # Stores the last seen index of each character
        l = 0          # Left pointer of the sliding window
        res = 0        # Maximum length found so far
        
        # Expand the window with the right pointer
        for r in range(len(s)):
            if s[r] in charMap:
                # If char repeats, move left pointer to skip past its last occurrence
                l = max(charMap[s[r]] + 1, l)
            
            # Update last seen index of current character
            charMap[s[r]] = r
            
            # Update result with the length of the current window
            res = max(res, r - l + 1)
        
        return res
