# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/

# Solution Approach

# Key Bit Operations:
# n & 1 - gets the rightmost bit
# n >> 1 - shifts bits right (moves them one position right)
# result << 1 - shifts bits left (makes room for new bit)
# result | bit - adds a bit to the result

# The Algorithm:
# Process each of the 32 bits
# Extract the rightmost bit from input
# Add it to our result (which we're building left-to-right)
# Shift input right to process next bit
# Shift result left to make room (except on last iteration)

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for _ in range(32):
            # Get the rightmost bit of n
            bit = n & 1
            
            # Shift result left to make room for new bit
            result = result << 1
            
            # Add the bit to result
            result = result | bit
            
            # Shift n right to process next bit
            n = n >> 1
        
        return result