# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/description/

# Intuition:
# 1. The "maximum product subarray" problem is tricky because multiplying by a negative
#    number can flip a small (negative) product into the largest one, and vice versa.
# 2. To handle this, we track both the maximum product so far (currentMax) 
#    and the minimum product so far (currentMin), since the min can become the max 
#    after multiplying with a negative number.
# 3. If we encounter a zero, the product resets (because any subarray containing zero 
#    will start fresh after that point).
# 4. At each step, we update the result with the best product seen so far.

# KEY INSIGHTS:
# - Track currentMax and currentMin at each step
# - Negative numbers swap the roles of max and min
# - Zero forces a reset (can't multiply through zero)
# - Need to consider starting fresh at each position (just the current number)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Track the min and max product ending at current position
        currentMin = 1
        currentMax = 1
        
        # Initialize result with max single element (handles all negative case)
        result = max(nums)

        for num in nums:
            # Zero breaks any subarray - reset both trackers
            if num == 0:
                currentMax, currentMin = 1, 1
                continue
            
            # Store currentMin before it gets updated (needed for currentMax calculation)
            temp =  num * currentMin
            
            # Update currentMin: choose SMALLEST of 3 options
            # 1. num * currentMax (could be very negative if both negative, or if currentMax positive & num negative)
            # 2. num * currentMin (could be positive if both negative, or very negative if signs differ)  
            # 3. num (start fresh subarray from current position)
            currentMin = min(num * currentMax, num * currentMin, num)
            
            # Update currentMax: choose best of 3 options  
            # 1. num * currentMax (extend positive product)
            # 2. temp (num * old currentMin - if both negative, becomes positive)
            # 3. num (start fresh subarray from current position)
            currentMax = max(num * currentMax, temp, num)
            
            # Update global result with current maximum
            result = max(currentMax, result)
            
        return result