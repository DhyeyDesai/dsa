# 1899. Merge Triplets to Form Target Triplet
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/

# INTUITION:
# The merge operation takes max of each position: [a,b,c] + [d,e,f] = [max(a,d), max(b,e), max(c,f)]
# Key insight: Once a value exceeds target at ANY position, we can NEVER reduce it back down.

# Strategy:
# 1. Filter out "bad" triplets - any triplet with a value > target at any position
#    (these would ruin our result if merged)
# 2. Track which target positions we can achieve using only "good" triplets
# 3. If we can match all 3 positions of the target, return true

# Why this works:
# - We only consider triplets that won't overshoot the target
# - We check if these safe triplets collectively contain each target value
# - Since max operation can only increase/maintain values, finding all 3 positions means
#   we can build the target by merging the right combination of good triplets

# Time: O(n) - single pass through triplets
# Space: O(1) - set stores at most 3 indices

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Track which positions of target we've successfully matched        
        good = set()

        for t in triplets:
            # Skip "bad" triplets that exceed target at any position
            # If we merge these, we'd overshoot and can never recover
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]: 
                continue
            
            # This is a "good" triplet - check which target positions it matches
            for i, n in enumerate(t):
                if n == target[i]:
                    # Mark this position as achievable
                    good.add(i)
            
        # Success if we found matches for all 3 positions (indices 0, 1, 2)
        return len(good) == 3