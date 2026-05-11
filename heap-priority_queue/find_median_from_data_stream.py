# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/description/

# ═══════════════════════════════════════════════════════════════
# INTUITION
# ═══════════════════════════════════════════════════════════════
# To find the median at any point, we need quick access to the
# middle element(s) of a sorted stream — without actually sorting
# on every insertion.
#
# The trick: split the numbers into two halves using two heaps.
#
#   small (max-heap) — holds the lower half of numbers
#   large (min-heap) — holds the upper half of numbers
#
# We maintain two invariants after every insertion:
#   1. ORDER:   every number in small <= every number in large
#   2. BALANCE: the heaps differ in size by at most 1
#
# With these invariants, the median is always at the tops:
#   - Equal sizes   → average of both tops
#   - small is bigger → top of small
#   - large is bigger → top of large
#
# Python only has a min-heap, so we simulate a max-heap for
# `small` by storing values negated (-num).
#
# ═══════════════════════════════════════════════════════════════


# ───────────────────────────────────────────────────────────────
# Time  : O(log n) per addNum — heap push/pop operations
#         O(1)     per findMedian — just peek at heap tops
# Space : O(n) — storing all n numbers across both heaps
# ───────────────────────────────────────────────────────────────
import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max-heap (lower half) — values stored negated
        self.large = []  # min-heap (upper half)

    def addNum(self, num: int) -> None:
        # Always push to small first (negate to simulate max-heap)
        heapq.heappush(self.small, -1 * num)

        # Invariant 1 — enforce ORDER:
        # If the largest in small exceeds the smallest in large,
        # the halves are out of order — move the offending element over
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Invariant 2 — enforce BALANCE:
        # If either heap is more than 1 element ahead, rebalance
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # Odd total — the larger heap holds the middle element
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        # Even total — median is the average of the two middle elements
        return (-1 * self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()