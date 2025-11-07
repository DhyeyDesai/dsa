# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/

# INTUITION:
# 1. Use sliding window: expand right to find valid window, shrink left to minimize it
# 2. Track character frequencies: countT (target), window (current window)
# 3. have/need pattern: have = unique chars with enough frequency, need = total unique chars in t
# 4. When have == need, we have a valid window - try to shrink it from left
# 5. Keep track of smallest valid window found
#
# Time Complexity: O(m + n) where m = len(s), n = len(t) - each char visited at most twice
# Space Complexity: O(m + n) for the hashmaps (worst case all unique characters)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: empty target string
        if t == "":
            return ""
        
        # countT: frequency map of characters in target string t
        # window: frequency map of characters in current window
        countT, window = {}, {}

        # Build frequency map for target string
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have: number of unique characters in window with desired frequency
        # need: number of unique characters required (total unique chars in t)
        have, need = 0, len(countT)

        # res: stores [left, right] indices of minimum window
        # resLen: length of minimum window found so far
        res, resLen  = [-1, -1], float("inf")
        
        # Left pointer for sliding window
        l = 0

        # Expand window by moving right pointer
        for r in range(len(s)):
            c = s[r]
            
            # Add current character to window
            window[c] = 1 + window.get(c, 0)

            # Check if we've met the frequency requirement for this character
            # Only increment 'have' when frequency MATCHES (not exceeds)
            if c in countT and window[c] == countT[c]:
                have+=1
            
            # Contract window from left while it's valid (have == need)
            while have == need:
                # Update result if current window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # Remove leftmost character from window
                window[s[l]] -= 1
                
                # If removing this character breaks a requirement, decrement 'have'
                if s[l]  in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                # Move left pointer forward (shrink window)
                l+=1
        
        # Extract and return the minimum window substring
        l, r = res
        return s[l:r+1]
