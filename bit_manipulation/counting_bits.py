# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/


# INTUITION:
# 1. Use DP to avoid recounting bits - leverage previously computed results
# 2. Key pattern: numbers follow a repeating structure based on powers of 2
# 3. Insight: For any number i, it's 1-bit count = 1 + count of (i - most_significant_bit)
# 4. The "offset" tracks the most significant bit (largest power of 2 ≤ i)

# BIT PATTERN OBSERVATION:
# 0:  0000 → 0 bits
# 1:  0001 → 1 bit  (offset=1)
# 2:  0010 → 1 bit  (offset=2, pattern resets)
# 3:  0011 → 2 bits (0010 + 1 = dp[3-2] + 1 = dp[1] + 1)
# 4:  0100 → 1 bit  (offset=4, pattern resets again)
# 5:  0101 → 2 bits (0100 + 1 = dp[5-4] + 1 = dp[1] + 1)
# 6:  0110 → 2 bits (0100 + 10 = dp[6-4] + 1 = dp[2] + 1)
# 7:  0111 → 3 bits (0100 + 11 = dp[7-4] + 1 = dp[3] + 1)

# KEY INSIGHT: When we reach a power of 2, the pattern repeats with +1 bit


class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp[i] = number of 1-bits in binary representation of i
        dp = [0] * (n + 1)
        offset = 1  # Tracks the most significant bit (current power of 2)

        for i in range(1, n + 1):
            # Check if we've reached the next power of 2
            # When offset*2 == i, we have a new most significant bit
            if offset * 2 == i:
                offset = i  # Update offset to new power of 2
            
            # Count for i = 1 (for new MSB) + count for (i - offset)
            # Essentially: remove MSB and look up the remaining pattern
            dp[i] = 1 + dp[i - offset]
        
        return dp