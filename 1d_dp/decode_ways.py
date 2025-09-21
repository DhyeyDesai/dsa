# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/description/


# Solution 1: DP - Bottom-Up with Hash Map
class Solution:
    def numDecodings(self, s: str) -> int:
        
        # INTUITION:
        # 1. Work backwards from end of string - if we know ways to decode suffix, 
        #    we can calculate ways for current position
        # 2. At each position, we have 1-2 choices: take 1 digit or 2 digits (if valid)
        # 3. Single digit: valid if not '0' (maps to A-I)
        # 4. Two digits: valid if "10"-"26" (maps to J-Z)  
        # 5. Base case: empty string has exactly 1 way to decode (decode nothing)
        
        n = len(s)
        # dp[i] = number of ways to decode string starting from index i
        # Base case: empty suffix (beyond string end) has 1 way
        ways_from_pos = {n: 1}
        
        # Process each position from right to left
        for pos in range(n - 1, -1, -1):
            # If current character is '0', it cannot be decoded alone
            if s[pos] == "0":
                ways_from_pos[pos] = 0
            else:
                # Option 1: Decode single digit (always valid for '1'-'9')
                ways_from_pos[pos] = ways_from_pos[pos + 1]
            
            # Option 2: Try to decode two digits if possible
            if (pos + 1 < n and 
                (s[pos] == "1" or  # "10"-"19" are all valid
                 (s[pos] == "2" and s[pos + 1] in "0123456"))):  # "20"-"26" are valid
                ways_from_pos[pos] += ways_from_pos[pos + 2]
                
        return ways_from_pos[0]


# Solution 2: DP - Bottom-Up (Space Optimized)
class Solution:
    def numDecodings(self, s: str) -> int:
        
        # INTUITION:
        # 1. Same logic as Solution 1, but optimize space usage
        # 2. Only need to track last 2 positions (current depends on next 1-2 positions)
        # 3. Use 3 variables instead of hash map: current, one_ahead, two_ahead
        # 4. Roll variables forward as we process each position
        # 5. Achieves O(1) space instead of O(n)
        
        n = len(s)
        
        # Variables to track DP states
        current_ways = 0    # ways to decode from current position
        one_step_ahead = 1  # ways to decode from position i+1 (initially: empty string)
        two_steps_ahead = 0 # ways to decode from position i+2
        
        # Process each position from right to left
        for pos in range(n - 1, -1, -1):
            # Reset current position calculation
            if s[pos] == "0":
                # '0' cannot be decoded as single digit
                current_ways = 0
            else:
                # Single digit decode: inherit ways from next position
                current_ways = one_step_ahead
            
            # Check if we can form valid two-digit number
            if (pos + 1 < n and 
                (s[pos] == "1" or  # "1X" where X is any digit
                 (s[pos] == "2" and s[pos + 1] in "0123456"))):  # "20" to "26"
                # Add ways from two positions ahead
                current_ways += two_steps_ahead
            
            # Shift variables for next iteration
            # Update: two_ahead <- one_ahead <- current, reset current
            current_ways, one_step_ahead, two_steps_ahead = 0, current_ways, one_step_ahead
            
        return one_step_ahead