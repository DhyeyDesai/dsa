# 312. Burst Balloons
# https://leetcode.com/problems/burst-balloons/

# ═══════════════════════════════════════════════════════════════
# INTUITION
# ═══════════════════════════════════════════════════════════════
# Greedy fails here because bursting a balloon changes its neighbors,
# creating complex dependencies. The key insight is to think in reverse:
# instead of asking "which balloon do I burst first?", ask
# "which balloon do I burst LAST in this range?"
#
# If balloon k is the last to be burst in range (i, j), then when
# we burst it, the only neighbors remaining are the boundaries i and j.
# This makes the coin calculation clean: nums[i] * nums[k] * nums[j].
# Better yet, the left (i, k) and right (k, j) subproblems become
# completely independent of each other — perfect for DP.
#
# We pad nums with 1s on both ends to handle edge boundaries cleanly.
#
# Recurrence:
#   dp[i][j] = max over all k in (i, j) of:
#              dp[i][k] + nums[i]*nums[k]*nums[j] + dp[k][j]
#
# ═══════════════════════════════════════════════════════════════


# ───────────────────────────────────────────────────────────────
# Solution 1 — Top-Down DP (Manual Memoization with 2D table)
#
# Time  : O(n³) — O(n²) subproblems, O(n) choices of k each
# Space : O(n²) — for the memoization table + O(n) recursion stack
# ───────────────────────────────────────────────────────────────
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad with 1s so boundary bursts don't go out of bounds
        nums = [1] + nums + [1]
        n = len(nums)

        # res[i][j] = max coins from bursting all balloons strictly between i and j
        res = [[0] * n for _ in range(n)]

        def recursion(i, j):
            # Base case: no balloons between i and j
            if j <= i + 1:
                return 0

            # Return cached result if already computed
            if res[i][j] != 0:
                return res[i][j]

            best = 0
            # Try every k as the LAST balloon to burst in (i, j)
            for k in range(i + 1, j):
                # k is last: its neighbors are just the boundaries i and j
                coins = nums[i] * nums[k] * nums[j]
                # Recurse independently on left and right subranges
                best = max(best, recursion(i, k) + coins + recursion(k, j))

            # Cache and return the best result for this range
            res[i][j] = best
            return best

        recursion(0, n - 1)
        return res[0][n - 1]  # Answer spans the full padded array


# ───────────────────────────────────────────────────────────────
# Solution 2 — Top-Down DP (@cache decorator)
#
# Identical logic to Solution 1, but @cache replaces the manual
# res table entirely — cleaner and less boilerplate.
# Since recursion() is defined inside maxCoins(), a fresh cache
# is created on every call, so no cache_clear() is needed.
#
# Time  : O(n³) — same as Solution 1
# Space : O(n²) — cache stores O(n²) subproblem results + O(n) stack
# ───────────────────────────────────────────────────────────────
from functools import cache

class Solution2:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad with 1s so boundary bursts don't go out of bounds
        nums = [1] + nums + [1]
        n = len(nums)

        # @cache automatically memoizes by (i, j) argument pair
        @cache
        def recursion(i, j):
            # Base case: no balloons between i and j
            if j <= i + 1:
                return 0

            best = 0
            # Try every k as the LAST balloon to burst in (i, j)
            for k in range(i + 1, j):
                # k is last: its neighbors are just the boundaries i and j
                coins = nums[i] * nums[k] * nums[j]
                # Recurse independently on left and right subranges
                best = max(best, recursion(i, k) + coins + recursion(k, j))

            return best

        # Kick off recursion over the full range (excluding padding)
        return recursion(0, n - 1)