# 66. Plus One
# https://leetcode.com/problems/plus-one/description/

"""
Intuition:
Adding 1 to a number represented as an array is like elementary addition with carries.
We start from the rightmost digit (least significant) and work our way left.

Key cases:
1. If current digit < 9: simply add 1 and we're done (no carry needed)
2. If current digit = 9: it becomes 0 and we carry 1 to the next position
3. If all digits are 9 (e.g., [9,9,9]): we get all 0s and need to prepend 1

The elegant part is that we only need to handle carries going left, and if we 
successfully add 1 without reaching the end, we can return immediately.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the rightmost digit (least significant)
        i = len(digits) - 1

        # Process digits from right to left
        while i >= 0:
            # If current digit is less than 9, we can simply add 1
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No carry needed, we're done!
            
            # Current digit is 9, so it becomes 0 and we carry 1
            digits[i] = 0
            i -= 1  # Move to the next digit (going left)
        
        # If we reach here, all original digits were 9
        # Example: [9,9,9] becomes [0,0,0], so we need [1,0,0,0]
        return [1] + digits