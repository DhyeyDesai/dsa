# 97. Interleaving String
# https://leetcode.com/problems/interleaving-string/

# INTUITION:
# 1. Use 2D DP where dp[i][j] represents: "Can we form s3[i+j:] using s1[i:] and s2[j:]?"
# 2. Work backwards from the end of strings to leverage already computed subproblems
# 3. At each position (i,j), we have two choices: take from s1[i] or s2[j]
# 4. A position is valid if either choice leads to a valid future state (dp[i+1][j] or dp[i][j+1])
# 5. Base case: dp[len(s1)][len(s2)] = True (both strings exhausted = valid interleaving)

# TIME COMPLEXITY: O(m * n) where m = len(s1), n = len(s2)
# SPACE COMPLEXITY: O(m * n) for the DP table

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Quick validation: lengths must add up
        if len(s1) + len(s2) != len(s3):
            return False
        
        # Create DP table: dp[i][j] = can we form s3[i+j:] from s1[i:] and s2[j:]
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]

        # Base case: when both strings are fully used, interleaving is valid 
        dp[len(s1)][len(s2)] = True

        # Fill DP table bottom-up (from end to start)   
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                # Option 1: Take character from s1
                # Check if: s1 has remaining chars AND s1[i] matches s3[i+j] AND taking s1[i] leads to valid state
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                
                # Option 2: Take character from s2
                # Check if: s2 has remaining chars AND s2[j] matches s3[i+j] AND taking s2[j] leads to valid state
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        
        # Answer is at dp[0][0]: can we form entire s3 starting from beginning of s1 and s2?
        return dp[0][0]
    


# 97. Interleaving String - Space Optimized DP
# https://leetcode.com/problems/interleaving-string/

# INTUITION:
# 1. Use 1D DP to track if remaining portions of s1 and s2 can form remaining s3
# 2. dp[j] represents: "Can we form s3[i+j:] using s1[i:] and s2[j:]?"
# 3. Use two arrays that alternate: current row (nextDp) and previous row (dp)
# 4. At each position, we can take a character from s1 OR s2 if it matches s3[i+j]
# 5. Work backwards from end to start, building solution from base case

# TIME COMPLEXITY: O(m * n) where m = len(s1), n = len(s2)
# SPACE COMPLEXITY: O(n) - only store two 1D arrays instead of full 2D table

class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        # Early exit: total length must match
        if m + n != len(s3):
            return False
        
        # Optimization: ensure m is the smaller dimension to minimize space
        if n < m:
            m, n = n, m
            s1, s2 = s2, s1  # Swap strings too
        
        # Previous row: dp[j] = can we form s3[i+j:] using s1[i:] and s2[j:]
        dp = [False] * (n + 1)
        
        # Base case: when both strings are exhausted, interleaving is complete
        dp[n] = True
        
        # Process each position in s1 from end to beginning
        for i in range(m, -1, -1):
            # Current row being computed
            nextDp = [False for _ in range(n + 1)]

            # Base case for when s1 is exhausted (i == m)
            if i == m:
                nextDp[n] = True

            # Process each position in s2 from end to beginning
            for j in range(n, -1, -1):
                
                # Option 1: Take character from s1
                # Check if: s1[i] matches s3[i+j] AND the state after taking s1[i] is valid
                # dp[j] contains dp[i+1][j] from previous iteration
                if i < m and s1[i] == s3[i+j] and dp[j]:
                    nextDp[j] = True
                
                # Option 2: Take character from s2
                # Check if: s2[j] matches s3[i+j] AND the state after taking s2[j] is valid
                # nextDp[j+1] contains dp[i][j+1] from current row
                if j < n and s2[j] == s3[i+j] and nextDp[j+1]:
                    nextDp[j] = True
            
            # Move to next iteration: current row becomes previous row
            dp = nextDp
        
        # Answer: can we form entire s3 starting from beginning of both strings?
        return dp[0]