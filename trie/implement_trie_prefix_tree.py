# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/description/

# TRIE EXPLANATION:
# A Trie (pronounced "try") is a tree data structure used for efficient string storage and retrieval.
# - Each node represents a character in a string
# - Paths from root to nodes form words/prefixes
# - Common prefixes share the same path, making it space-efficient for storing many words
# - Time complexity: O(m) for insert/search/startsWith, where m is the length of the word
# - Use cases: autocomplete, spell checkers, IP routing tables

class TrieNode:
    def __init__(self):
        self.children = {}  # Maps characters to child TrieNodes
        self.endOfWord = False  # Marks if a complete word ends at this node

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Empty root node to start the trie

    def insert(self, word: str) -> None:
        # Inserts a word into the trie by creating nodes for each character.
        # Time: O(m), Space: O(m) where m is word length

        cur = self.root
        
        # Traverse/create path for each character
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()  # Create new node if path doesn't exist
            cur = cur.children[c]  # Move to next node
        
        cur.endOfWord = True  # Mark the end of the inserted word

    def search(self, word: str) -> bool:
        # Returns True if the exact word exists in the trie.
        # Time: O(m), Space: O(1) where m is word length

        cur = self.root
        
        # Try to follow the path for each character
        for c in word:
            if c not in cur.children:
                return False  # Path doesn't exist
            cur = cur.children[c]
        
        # Word exists only if we reach a node marked as end of word
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        # Returns True if any word in the trie starts with the given prefix.
        # Time: O(m), Space: O(1) where m is prefix length

        cur = self.root
        
        # Try to follow the path for each character in prefix
        for c in prefix:
            if c not in cur.children:
                return False  # Prefix path doesn't exist
            cur = cur.children[c]
        
        # If we successfully traversed the prefix, it exists
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)