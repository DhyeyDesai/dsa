# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/description/

# Solution 1: Dynamic Programming (Optimal)

# INTUITION:
# This is a space-optimized version of edit distance. Instead of keeping a full 2D table,
# we only maintain a single array (the "current row" of the DP table). As we process each
# character of word1, we update this array in-place. We save the old value before 
# overwriting (nextDp) because we need it for the next calculation. We also ensure word1 
# is the longer word so our array is sized by the shorter word, minimizing space usage.

# TIME COMPLEXITY: O(m * n) - where m = len(word1), n = len(word2)
# SPACE COMPLEXITY: O(min(m, n)) - only one array of size equal to shorter word

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Ensure word1 is the longer word so dp array is sized by shorter word
        # This minimizes space usage: O(min(m,n)) instead of O(max(m,n))
        if m < n:
            word1, word2 = word2, word1
            m, n = n, m
        
        # Initialize dp array: dp[j] = operations to convert empty string to word2[j:]
        # Base case: if word1 is empty, insert all remaining chars from word2
        dp = [(n - i) for i in range(n + 1)]

        # Process each character of word1 from right to left
        for i in range(m - 1, -1, -1):
            # Save the rightmost value (represents dp[i+1][n] in 2D version)
            nextDp = dp[n]
            # Update rightmost position: operations to convert word1[i:] to empty string
            dp[n] = m - i
            
            # Process each character of word2 from right to left
            for j in range(n - 1, -1, -1):
                # Save current dp[j] before overwriting (this is dp[i+1][j] from 2D)
                temp = dp[j]
                
                # If characters match, no operation needed
                if word1[i] == word2[j]:
                    dp[j] = nextDp  # Use diagonal value (dp[i+1][j+1])
                else:
                    # Try all three operations and pick minimum:
                    # dp[j+1] = insert
                    # dp[j] = delete  
                    # nextDp = replace (diagonal from previous row)
                    dp[j] = 1 + min(dp[j+1], dp[j], nextDp)
                
                # Move the saved value to nextDp for next iteration
                # (it will be the diagonal for dp[j-1])
                nextDp = temp
        
        # dp[0] now contains min operations to convert word1 to word2
        return dp[0]


# Solution 2: Dynamic Programming (Bottom-Up)
# INTUITION:
# Edit distance measures the minimum operations (insert, delete, replace) needed to 
# convert word1 to word2. We use dynamic programming where cache[i][j] represents the 
# minimum operations needed to convert word1[i:] to word2[j:]. If characters match, 
# no operation needed. Otherwise, try all three operations and pick the minimum.

# TIME COMPLEXITY: O(m * n) - where m = len(word1), n = len(word2)
# SPACE COMPLEXITY: O(m * n) - 2D DP table

class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        # Create DP table: cache[i][j] = min operations to convert word1[i:] to word2[j:]
        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # Base case: if word1 is exhausted, need to insert all remaining chars of word2
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        
        # Base case: if word2 is exhausted, need to delete all remaining chars of word1
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        # Fill DP table bottom-up (from end of strings to beginning)
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                # If characters match, no operation needed
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    # Try all three operations and pick minimum:
                    # cache[i][j+1] = insert char from word2
                    # cache[i+1][j] = delete char from word1
                    # cache[i+1][j+1] = replace char in word1
                    cache[i][j] = 1 + min(cache[i][j+1], cache[i+1][j], cache[i+1][j+1])
        
        # Result: min operations to convert word1[0:] to word2[0:]
        return cache[0][0]

