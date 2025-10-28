# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/


# Solution 1: Min-Heap
# INTUITION:
# To find the kth largest, we need to track the k largest elements seen so far.
# Strategy: Use a min heap of size k.
# - The heap always contains the k largest elements processed so far
# - The ROOT of the heap is the SMALLEST of these k largest = kth largest overall
# - When we see a larger element, we evict the smallest (root) and add the new one

# Why min heap? Because we want quick access to the SMALLEST of our k largest elements
# to know when to evict it.

# Time: O(n log k) - n insertions, each log k
# Space: O(k)

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
    


# Solution 2: Quick-select
class Solution2:
# INTUITION:
# QuickSelect is like QuickSort but we only recurse on ONE side - the side containing our target.

# Key insights:
# 1. Kth largest = (n-k)th smallest when 0-indexed
#    Example: 2nd largest in [1,2,3,4,5] = 3rd smallest (index 3) = 4
# 2. Partitioning puts pivot in its final sorted position
# 3. If pivot lands at position k, we found our answer!
# 4. Otherwise, we know which half contains our target and only search there

# Why it's faster than sorting:
# - QuickSort: O(n log n) - recursively sorts BOTH sides
# - QuickSelect: O(n) average - only recurses on ONE side, eliminating half each time

# Partition example: [3,2,1,5,6,4], pivot=4
# After partition: [3,2,1,4,6,5] - everything left of 4 is ≤4, everything right is >4
#                         ↑
#                     pivot at index 3

# Time Complexity: 
# - Average: O(n) - we eliminate ~half the array each recursion: n + n/2 + n/4 + ... ≈ 2n
# - Worst: O(n²) - if we always pick bad pivots (already sorted array)
#   Can be improved to O(n) guaranteed with median-of-medians, but adds complexity
# NOTE: Because of worst-case O(n²) behavior when the array is already sorted or nearly sorted,
# there's a chance of getting TLE (Time Limit Exceeded) on LeetCode.
# One way to tackle this is using 3-Way Partitioning (For Duplicate-Heavy Arrays) like in Solution 3

# Space Complexity: 
# - O(1) - in-place partitioning, modifies input array
# - O(log n) average recursion depth (worst case O(n) with bad pivots)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert kth largest to index: kth largest = (n-k)th element in sorted order
        k = len(nums) - k

        def quickSelect(l, r):
            # Choose rightmost element as pivot (could randomize for better average case)
            pivot, p = nums[r], l

            # Partition: move all elements ≤ pivot to the left
            for i in range(l, r):
                if nums[i] <= pivot:
                    # Swap smaller element to position p (left section)
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
            # Place pivot in its final sorted position
            # Everything left of p is ≤ pivot, everything right is > pivot
            nums[p], nums[r] = nums[r], nums[p]

            # Now nums[p] is in its correct sorted position!
            if p>k:
                # Target is in the left half (smaller elements)
                return quickSelect(l, p-1)
            elif p<k:
                # Target is in the right half (larger elements)
                return quickSelect(p+1, r)
            else:
                # Found it! nums[p] is the kth smallest (or (n-k)th largest)
                return nums[p]
        
        return quickSelect(0, len(nums)-1)
    


# Three-way QuickSelect with random pivot selection.

# Time Complexity: O(n) average, O(n²) worst case
# - Average: n + n/2 + n/4 + ... ≈ 2n = O(n) with random pivots
# - Worst: O(n²) is theoretically possible but probability is ~1/n! (astronomically rare)
# - Random pivot makes worst case virtually impossible in practice

# Space Complexity: O(1) auxiliary space (in-place partitioning)
# - Recursion stack: O(log n) average depth, O(n) worst case depth

# Why O(n²) isn't a problem:
# - Deterministic pivot (always rightmost) + sorted array = guaranteed O(n²) ❌
# - Random pivot + ANY array = O(n²) probability ≈ 1/n! ≈ 0.0000...0001% ✅
# - Even adversarial inputs can't force bad behavior with true randomization

import random

class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            # Three-way partition: randomly pick pivot, then partition array into
            # [elements < pivot | elements = pivot | elements > pivot]
            # Only recurse on the section containing our target index k
           

            # Pick random pivot VALUE
            pivot = nums[random.randint(l, r)]
            
            # Three pointers for three-way partitioning
            # i tracks position for next "less than" element
            # j scans through array
            # t tracks position for next "greater than" element (from right)
            i, j, t = l, l, r
            
            while j <= t:
                if nums[j] < pivot:
                    # Move smaller element to left section
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                elif nums[j] > pivot:
                    # Move larger element to right section
                    nums[j], nums[t] = nums[t], nums[j]
                    t -= 1  # Don't increment j - need to check swapped element
                else:
                    # Equal to pivot, just move forward
                    j += 1
            
            # Result: [l..i-1] < pivot | [i..t] = pivot | [t+1..r] > pivot
            if k < i:
                return quickSelect(l, i - 1)
            elif k > t:
                return quickSelect(t + 1, r)
            else:
                return pivot
        
        return quickSelect(0, len(nums) - 1)