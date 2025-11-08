# 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/

# INTUITION:
# 1. We need the maximum in every window of size k, but recalculating max each time is O(k) - too slow
# 2. Use a deque to maintain indices of potential maximums in DECREASING order of their values
# 3. Key insight: If a new number is larger than previous numbers, those previous numbers can NEVER
# be the maximum (even in future windows), so remove them from consideration
# 4. The front of the deque always contains the index of the current window's maximum

# TIME COMPLEXITY: O(n) - each element is added and removed from deque at most once
# SPACE COMPLEXITY: O(k) - deque stores at most k indices

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = 0  # Left pointer of the sliding window
        r = 0  # Right pointer of the sliding window
        q = deque()  # Stores indices in decreasing order of their values

        while r < len(nums):
            # Remove all smaller elements from the back of deque
            # They can never be maximum as long as nums[r] is in the window
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # Add current index to deque
            q.append(r)

            # Remove left index from deque if it's outside the window
            # q[0] holds the index of the maximum element
            if l > q[0]:
                q.popleft()
            
            # Once we have a complete window of size k, record the maximum
            if (r+1) >= k:
                # q[0] is the index of maximum element in current window
                output.append(nums[q[0]])
                l+=1 # Slide the window's left boundary

            r += 1 # Expand the window's right boundary


        return output