# 115. Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/description/

# Intuition:
# At each position in s, we have two choices: skip the current character, or
# (if it matches the current character in t) use it to match. We recursively
# count both paths and sum the results. Memoization ensures each (i, j) pair
# is computed only once.
#
# Time Complexity:  O(m * n) — m = len(s), n = len(t); each (i, j) state is computed once
# Space Complexity: O(m * n) — for the memoization cache + O(m + n) recursion stack depth

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i, j):
            # Return cached result if this subproblem was already solved
            if (i, j) in cache:
                return cache[(i, j)]

            # All characters in t have been matched — valid subsequence found
            if j == len(t):
                cache[(i, j)] = 1
                return 1

            # Exhausted s but t still has unmatched characters — dead end
            if i == len(s):
                cache[(i, j)] = 0
                return 0

            # Choice 1: always skip s[i] (don't use it for matching)
            res = dfs(i + 1, j)

            # Choice 2: if s[i] matches t[j], also try using it to advance in t
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)

            cache[(i, j)] = res
            return res

        return dfs(0, 0)