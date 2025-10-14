# 703. Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

# Intuition:
# We don't need all elements, just the k largest.
# So we maintain a min-heap of size k.
# The top (root) of the heap is the Kth largest, since the other k-1 elements in the heap are larger than it.
# Every time a new number comes:
# Add it
# If heap grows beyond k, remove the smallest
# The root remains the updated Kth largest

# Time complexity:
# Each insertion into the heap takes O(log k) time. Since there are n elements in total, the time complexity is O(n log k).

# Space complexity:
# The space complexity is O(k) because we store at most k elements in the heap.

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        
        # Convert the input list into a valid min-heap in O(n) time
        heapq.heapify(self.nums) 
        
        # Keep only the top k largest elements in the heap.
        # If size exceeds k, pop the smallest values until only k remain.
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # Push the new value into the heap (still a min-heap)
        heapq.heappush(self.nums, val)

        # If size exceeds k, remove the smallest element
        # so only the k largest elements remain.
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        # The smallest element in this heap is the Kth largest overall
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)