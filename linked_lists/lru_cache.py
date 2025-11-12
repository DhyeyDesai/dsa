# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/

"""
INTUITION:
1. Use HashMap for O(1) access to cache entries by key
2. Use Doubly Linked List to maintain LRU order: left = LRU, right = MRU
3. Dummy nodes at both ends eliminate edge cases when inserting/removing nodes
4. On access/update: move node to right (MRU). On eviction: remove from left (LRU)

TIME COMPLEXITY: O(1) for both get() and put()
SPACE COMPLEXITY: O(capacity) for storing cache entries
"""

class Node:
    """
    Node in doubly linked list representing a cache entry.
    Stores key (needed for eviction from hashmap) and value.
    """
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    """
    INTUITION:
    - Combine HashMap (for O(1) lookup) with Doubly Linked List (for O(1) reordering)
    - Maintain order: [LEFT(dummy)] ←→ [LRU] ←→ ... ←→ [MRU] ←→ [RIGHT(dummy)]
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node mapping for O(1) access
        
        # Create dummy boundary nodes to avoid edge cases
        # left = LRU side, right = Most Recently Used side
        self.left, self.right = Node(0, 0), Node(0, 0)
        # Link dummy nodes together to form empty list
        self.left.next, self.right.prev = self.right, self.left
        

    def insert(self, node):
        """
        INTUITION:
        - Insert at right (before right dummy) = mark as most recently used
        - Update 4 pointers to splice node into the list
        """
        # Get nodes that will surround the new node
        prev, nxt = self.right.prev, self.right
        
        # Update pointers: prev ←→ node ←→ nxt
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    
    def remove(self, node):
        """
        INTUITION:
        - Remove node from its current position by linking its neighbors together
        - Update 2 pointers to bypass the node
        """
        # Get neighboring nodes
        prev = node.prev
        nxt = node.next
        
        # Bypass the node: prev ←→ nxt
        prev.next = nxt
        nxt.prev = prev
    
    def get(self, key: int) -> int:
        """
        INTUITION:
        - If key exists: move to right (MRU position) and return value
        - If not: return -1
        """
        if key in self.cache:
            # Mark as recently used by moving to right end
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1
        

    def put(self, key: int, value: int) -> None:
        """
        INTUITION:
        - If key exists: remove old node (will be replaced)
        - Insert new/updated node at right (MRU position)
        - If over capacity: evict LRU node from left
        """
        # If updating existing key, remove old node first
        if key in self.cache:
            self.remove(self.cache[key])
        
        # Create new node and add to cache and list
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])  # Insert at right (MRU position)

        # Check if we exceeded capacity
        if len(self.cache) > self.cap:
            # Evict LRU: leftmost real node (not the dummy)
            # Remember: left and right are dummy nodes
            # So left.next is the first REAL node = LRU
            lru = self.left.next
            
            # Remove from both list and hashmap
            self.remove(lru)
            del self.cache[lru.key]


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)