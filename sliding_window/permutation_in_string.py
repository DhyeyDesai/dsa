# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/

# INTUITION:
# 1. A permutation means same characters with same frequencies
# 2. Use fixed-size sliding window of length len(s1) on s2
# 3. Compare character frequencies of window with s1
# 4. Track "matches" - how many characters have matching frequencies
# 5. When matches == 26, we found a permutation!


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: s1 longer than s2, impossible to have permutation
        if len(s1) > len(s2): return False

        # Frequency arrays for s1 and current window in s2
        # Using arrays instead of hashmaps for O(1) lookups
        s1Count = [0] * 26
        s2Count = [0] * 26

        # Build frequency map for s1 and initial window in s2        
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Count how many characters (out of 26) have matching frequencies        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        # Slide the window across s2
        l = 0  # Left pointer of window
        for r in range(len(s1), len(s2)):
            # If all 26 characters match, we found a permutation
            if matches == 26:
                return True
            
            # Add new character (right side of window)
            index = ord(s2[r]) - ord('a')
            s2Count[index]+=1
            
            # Check if this addition created or broke a match
            if s2Count[index] == s1Count[index]:
                matches+=1 # Now matches!
            elif s2Count[index] == s1Count[index] + 1:
                matches-=1 # Was matching before, now broken
            
            # Remove old character (left side of window)
            index  = ord(s2[l]) - ord('a')
            s2Count[index]-=1
            
            # Check if this removal created or broke a match
            if s2Count[index] == s1Count[index]:
                matches+=1 # Now matches!
            elif s2Count[index] == s1Count[index] - 1:
                matches-=1 # Was matching before, now broken
            
            # Move left pointer to maintain window size
            l+=1
        
        return matches == 26


        