# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/




# Solution 1 - Greedy + Math (Preferred)
# INTUITION:
# The most frequent task creates a "framework" that determines minimum time.
# If task A appears 5 times with cooldown n=2, we need: A _ _ A _ _ A _ _ A _ _ A
# These gaps MUST exist - they're non-negotiable!

# KEY INSIGHTS:
# 1. Most frequent task forces us to create (max_freq - 1) chunks of size (n + 1)
# 2. Last occurrence doesn't need cooldown, so we add max_count tasks at the end
# 3. If we have enough task variety, no idle time needed → answer is just len(tasks)

# TIME AND SPACE COMPLEXITY:
# O(N) time: Linear pass through tasks + constant work on 26-element array
# O(1) space: Fixed 26-slot array regardless of input size

# FORMULA: max(len(tasks), (max_freq - 1) * (n + 1) + max_count)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequency of each task (A-Z)
        freq  = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] +=1

        # Find the highest frequency among all tasks
        max_freq = max(freq)
    
        # Count how many tasks share this max frequency
        # (they all need to appear in the final position)
        max_count = freq.count(max_freq)
        
        # Framework time: (max_freq-1) chunks of (n+1) size + max_count tasks at end
        # Actual time: len(tasks) if we have enough variety (no idle needed)
        # Take the maximum of both
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)



# Solution 2 - Heap
# INTUITION:
# Use a max-heap to always process the most frequent task available.
# When a task is used, it goes into a "cooldown queue" and re-enters 
# the heap once its cooldown expires.

# KEY DATA STRUCTURES:
# 1. Max-Heap: Stores available tasks by frequency (most frequent at top)
# 2. Queue: Stores tasks in cooldown as (available_time, frequency) pairs

# ALGORITHM FLOW:
# 1. Pop most frequent task from heap
# 2. Use it once (decrement frequency)
# 3. If still has occurrences, add to cooldown queue
# 4. Check if any task in queue is ready → push back to heap
# 5. If heap empty but queue has tasks → we're idle
# 6. Repeat until both heap and queue are empty

# WHY HEAP WORKS:
# - Heap gives us O(log k) access to most frequent task
# - Always processing highest frequency minimizes future idles
# - Queue naturally handles the cooldown timing

# TIME COMPLEXITY: O(N log k) where N = tasks, k = unique tasks
# - Each task enters/exits heap once: O(k log k)
# - Process N tasks total with heap operations: O(N log k)
# - In practice, k ≤ 26, so effectively O(N)

# SPACE COMPLEXITY: O(k) where k = unique tasks
# - Heap stores at most k unique tasks
# - Queue stores at most k tasks in cooldown
# - k ≤ 26, so effectively O(1)
import heapq
from collections import Counter, deque
class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequency of each task
        freq = Counter(tasks)

        # Create max-heap with negative frequencies (Python has min-heap)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        # Queue to store tasks in cooldown: (available_time, frequency)
        cooldown_queue = deque()
        
        time = 0

        # Continue until both heap and queue are empty
        while max_heap or cooldown_queue:
            time+=1

            # If heap has tasks, process the most frequent one
            if max_heap:
                # Pop most frequent task (remember it's negative)
                freq_neg = heapq.heappop(max_heap)
                freq_neg += 1  # Use once (increment because negative)

                # If task still has occurrences, put in cooldown queue.
                if freq_neg != 0:
                    cooldown_queue.append((time+n, freq_neg))
            
            # Check if any task in cooldown is now available
            if cooldown_queue and cooldown_queue[0][0] == time:
                available_time, freq_neg = cooldown_queue.popleft()
                heapq.heappush(max_heap, freq_neg)
        
        return time