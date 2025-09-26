# 139. Word Break
# https://leetcode.com/problems/word-break/description/


# INTUITION:
# 1. Bottom-up DP: work backwards from end of string to beginning
# 2. dp[i] = "can we break s[i:] into valid words from dictionary?"
# 3. For each position, try every word in dictionary as potential next word
# 4. If word matches AND the rest can be broken (dp[i+len(word)]), then dp[i] = True

# KEY INSIGHTS:
# - Base case: dp[len(s)] = True (empty string can always be "broken")
# - Work backwards so when we check dp[i+len(word)], it's already computed
# - Early termination: once we find one valid word at position i, we're done


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = True if s[i:] can be segmented into words from wordDict
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case: empty string can always be broken
        
        # Work backwards from end of string
        for i in range(len(s) - 1, -1, -1):
            # Try each word in dictionary at current position
            for word in wordDict:
                # Check if word fits within remaining string bounds
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    # If current word matches AND rest of string can be broken
                    dp[i] = dp[i + len(word)]
                
                # Early termination: found valid segmentation at position i
                if dp[i]:
                    break
        
        # dp[0] = True means entire string s[0:] can be segmented
        return dp[0]