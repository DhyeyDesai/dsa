# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/

# Solution 1
# INTUITION:
# 1. Count the number of 1-bits by examining each bit position
# 2. Use bit manipulation: check rightmost bit, then shift right to examine next bit
# 3. Continue until all bits are processed (n becomes 0)
# 4. Alternative approach: n & 1 to check last bit, n >> 1 to shift right

# ALGORITHM BREAKDOWN:
# - n % 2 gives us the rightmost bit (0 or 1)
# - n >> 1 shifts all bits right by 1 position (equivalent to n // 2)
# - Keep processing until n becomes 0 (no more bits to check)

# EXAMPLE: n = 11 (binary: 1011)
# Step 1: 1011 % 2 = 1, count = 1, n becomes 101
# Step 2: 101 % 2 = 1, count = 2, n becomes 10  
# Step 3: 10 % 2 = 0, count = 2, n becomes 1
# Step 4: 1 % 2 = 1, count = 3, n becomes 0
# Result: 3 one-bits

class Solution1:
    def hammingWeight(self, n: int) -> int:
        res = 0  # Counter for number of 1-bits
        
        # Process each bit until n becomes 0
        while n:
            # Check if rightmost bit is 1
            # n % 2 extracts the least significant bit (0 or 1)
            res += n % 2
            print("-->", n)
            # Shift right by 1 position to examine next bit
            # n >> 1 is equivalent to n // 2, moves all bits right
            n = n >> 1
            print(n)
            
        return res
    
# Solution 2
# INTUITION - BRIAN KERNIGHAN'S ALGORITHM:
# 1. Instead of checking every bit, we directly jump to and eliminate 1-bits
# 2. Key insight: n & (n-1) removes the rightmost 1-bit from n
# 3. We only iterate for the number of 1-bits, not all bit positions
# 4. Much more efficient for sparse numbers (few 1-bits)

# HOW n & (n-1) WORKS:
# - When we subtract 1 from n, all trailing zeros become 1, and the rightmost 1 becomes 0
# - The AND operation then zeros out everything from the rightmost 1-bit onwards
# - This effectively "turns off" the rightmost 1-bit

# EXAMPLE: n = 12 (binary: 1100)
# n = 1100, n-1 = 1011
# n & (n-1) = 1100 & 1011 = 1000 (removed rightmost 1)

# n = 1000, n-1 = 0111  
# n & (n-1) = 1000 & 0111 = 0000 (removed last 1)

# Result: 2 iterations = 2 one-bits


class Solution2:
    def hammingWeight(self, n: int) -> int:
        res = 0  # Counter for number of 1-bits
        
        # Continue until all 1-bits are eliminated
        while n:
            # Brian Kernighan's trick: remove the rightmost 1-bit
            # n & (n-1) clears the lowest set bit
            n = n & (n-1)
            
            # Each iteration removes exactly one 1-bit
            res += 1
            
        return res