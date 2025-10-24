# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

# INTUITION:
# 1. Use sliding window: expand right, shrink left when invalid
# 2. Valid window condition: (window_length - most_frequent_char) <= k
#    This means we can replace all non-frequent chars with at most k operations
# 3. Track historical max frequency (maxf) - not necessarily current window's max
# 4. Window size becomes "sticky" - only grows when we find better conditions
# 5. This works because we only care about finding LONGER valid windows,
#    not all valid windows
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}  # Frequency map of characters in current window
        res = 0     # Result: longest valid window length found
        l = 0       # Left pointer of sliding window
        maxf = 0    # Historical maximum frequency of any character we've seen
        
        for r in range(len(s)):
            # Expand window: add right character and update its frequency
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # Update maxf if current character's frequency is higher
            # This is O(1) instead of checking all frequencies O(26)
            maxf = max(maxf, count[s[r]])
            
            # Check if current window is invalid
            # (window_length - max_frequency) = characters we need to replace
            # If this exceeds k, we need to shrink the window
            while (r - l + 1) - maxf > k:
                # Shrink window: remove left character and decrease its frequency
                count[s[l]] -= 1
                l += 1
                # Note: We don't update maxf when shrinking - we keep historical max
            
            # Update result with current window length
            # Window is guaranteed to be valid OR same size as previous best
            res = max(r - l + 1, res)
        
        return res