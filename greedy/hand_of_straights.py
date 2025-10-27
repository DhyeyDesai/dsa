# 846. Hand of Straights
# https://leetcode.com/problems/hand-of-straights/


# INTUITION:
# 1. To form consecutive groups, we must start with the smallest available card
# 2. Once we pick the smallest card, we're forced to pick the next (groupSize-1) consecutive cards
# 3. If any consecutive card is missing or already used up, it's impossible to form valid groups
# 4. We use a min-heap to always access the smallest unused card efficiently
# 5. Cards must be removed from heap in sorted order - if we skip a card, it means we can't form a valid group

import heapq
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Check if total cards can be evenly divided into groups
        if len(hand) % groupSize:
            return False
        
        # Count frequency of each card
        hashMap = {}
        for h in hand:
            hashMap[h] = hashMap.get(h, 0) + 1
        
        # Create a min-heap with all unique card values
        values = list(hashMap.keys())
        heapq.heapify(values)
        
        # Keep forming groups until all cards are used
        while values:
            # Get the smallest available card (must be the start of a group)
            minValue = values[0]
            
            # Try to form a consecutive group starting from minValue
            for j in range(groupSize):
                card = minValue + j
                
                # Check if the required consecutive card exists and is available
                if card not in hashMap or hashMap[card] == 0:
                    return False
                
                # Use one instance of this card
                hashMap[card] -= 1
                
                # If this card is exhausted, remove it from the heap
                if hashMap[card] == 0:
                    # CRITICAL: The exhausted card must be at the top of heap
                    # If not, it means we skipped a smaller card, making valid groups impossible
                    if card != values[0]:
                        return False
                    heapq.heappop(values)
        
        # Successfully formed all groups
        return True


"""
TIME COMPLEXITY: O(n * log(n) + n * k)
- Building hashMap: O(n)
- Heapifying unique values: O(m * log(m)) where m = number of unique cards ≤ n
- Main loop: We process each card once, and for each card:
  - Heap operations (pop): O(log(m))
  - We do this n times total across all iterations
- Overall: O(n * log(n)) where n is the number of cards

SPACE COMPLEXITY: O(n)
- hashMap stores at most n unique cards: O(n)
- Heap stores at most n unique values: O(n)
- Overall: O(n)
"""