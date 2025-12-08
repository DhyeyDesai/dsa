# 127. Word Ladder
# https://leetcode.com/problems/word-ladder/

# INTUITION:
# This is a shortest path problem, so we use BFS (level-by-level search).
# Key insight: Instead of comparing every word with every other word (slow!),
# we create "patterns" by replacing each character with '*'.
# Words that share a pattern differ by only one letter, so they're neighbors.
# Example: "hit" creates patterns: "*it", "h*t", "hi*"
#          "hot" creates patterns: "*ot", "h*t", "ho*"
#          They share "h*t", so they're one transformation apart!

# TIME COMPLEXITY: O(M^2 * N) where M = word length, N = number of words
# - Building adjacency list: O(M^2 * N) - for each word, create M patterns of length M
# - BFS: O(M^2 * N) - in worst case, visit all words and check all their patterns
# SPACE COMPLEXITY: O(M^2 * N)
# - Adjacency list stores all patterns and their words
# - Queue and visited set can hold up to N words

from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Early exit: if endWord isn't in wordList, transformation impossible
        if endWord not in wordList:
            return 0
        
        # Build adjacency list using patterns
        # adj[pattern] = list of words matching that pattern
        adj = defaultdict(list)
        wordList.append(beginWord) # Include beginWord in our graph

        # For each word, generate all possible patterns and map them
        for word in wordList:
            for j in range(len(word)):
                # Create pattern by replacing character at position j with '*'
                pattern = word[:j] + '*' + word[j+1:]
                adj[pattern].append(word)
        
        # BFS setup
        res = 1 # Start at 1 because we're counting sequence length (includes beginWord)
        q = deque([beginWord]) # Queue for BFS, start with beginWord
        visit = set([beginWord]) # Track visited words to avoid cycles
        
        # BFS: process level by level
        while q:
            # Process all words at the current level (same distance from beginWord)
            for i in range(len(q)):
                word = q.popleft()
                
                # Found the endWord! Return current distance
                if word == endWord:
                    return res
                
                # Explore all neighbors (words that differ by one letter)
                for j in range(len(word)):
                    # Generate pattern for current word
                    pattern = word[:j] + '*' + word[j+1:]
                    
                    # Check all words that match this pattern
                    for nei in adj[pattern]:
                        if nei not in visit:
                            q.append(nei)  # Add to queue for next level
                            visit.add(nei)  # Mark as visited
            
            # Finished processing current level, increment distance for next level
            res += 1
        
        # If we exit the loop, endWord was never reached
        return 0

        