# 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}  # Maps characters to child TrieNodes
        self.endOfWord = False  # Marks if a complete word ends here

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()  # Initialize empty Trie

    def addWord(self, word: str) -> None:
        # Standard Trie insertion - create path for each character.
        # Time: O(m), Space: O(m)

        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # Search with wildcard support - '.' matches any character.
        # Uses DFS to explore all possible paths when '.' is encountered.
        # Time: O(m) best case, O(26^m) worst case
        
        def dfs(j, root):
            # j: current index in word
            # root: current TrieNode to search from
            cur = root
            
            # Traverse remaining characters starting from index j
            for i in range(j, len(word)):
                c = word[i]
                
                if c == '.':
                    # Wildcard: try all possible children (backtracking)
                    for child in cur.children.values():
                        # Recursively search from next position with each child
                        if dfs(i + 1, child):
                            return True  # Found valid path
                    return False  # No valid path found from any child
                else:
                    # Regular character: follow single path
                    if c not in cur.children:
                        return False  # Path doesn't exist
                    cur = cur.children[c]
            
            # Check if we ended at a complete word
            return cur.endOfWord
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)