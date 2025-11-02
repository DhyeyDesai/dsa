# 763. Partition Labels
# https://leetcode.com/problems/partition-labels/description/


# INTUITION:
# 1. A partition is valid when all occurrences of characters in it are contained within it
# 2. For each character, we need to know its LAST occurrence in the string
# 3. As we scan left-to-right, we track the farthest position we must reach to include
#    all occurrences of characters seen so far
# 4. When current index reaches this farthest position, we can "cut" - all characters
#    in current partition are complete
# 5. Greedy works: we make the cut as soon as possible, creating smallest valid partitions

# TIME COMPLEXITY: O(N) - two passes through string
# SPACE COMPLEXITY: O(1) - at most 26 characters in lastIndex map

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        # First pass: record the last index of each character
        # This tells us the farthest we MUST go to include all occurrences
        for i,c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        size = 0  # Size of current partition
        end = 0   # Farthest index we must reach for current partition

        # Second pass: scan and determine partition boundaries
        for i, c in enumerate(s):
            size += 1 # Current character is part of this partition
            # Update the boundary: we must go at least until this char's last occurrence            
            end = max(end, lastIndex[c])

            # If we've reached the boundary, we can make a cut here
            # All characters in [start...i] have no occurrences beyond i
            if i == end:
                res.append(size) # Record partition size
                size = 0 # Reset for next partition

        return res

