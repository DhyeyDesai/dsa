# 212. Word Search II
# https://leetcode.com/problems/word-search-ii/

# INTUITION:
# - Naive approach: For each word, do a DFS search on the board → O(words × board_size × 4^word_length)
# - Better approach: Use a Trie to store all words, then do ONE DFS traversal
# - As we explore the board, we simultaneously traverse the Trie
# - If current character doesn't exist in Trie → stop immediately (prune invalid paths)
# - This way we search for all words at once and avoid exploring impossible paths

# TIME COMPLEXITY: O(M × N × 4^L)
# - M × N = board dimensions (we start DFS from each cell)
# - 4^L = worst case we explore all 4 directions up to max word length L
# - In practice, Trie pruning makes this much faster

# SPACE COMPLEXITY: O(K × L)
# - K = number of words, L = average word length (for Trie storage)
# - O(L) for recursion stack depth

class TrieNode:
    def __init__(self):
        self.children = {} # Maps character → TrieNode
        self.endOfWord = False # True if a word ends at this node

    def addWord(self, word):
        cur = self
        # Build path in Trie for each character
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True # Mark the end of a complete word
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build Trie from all words
        root = TrieNode()

        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set() # res: found words, visit: current path cells

        def dfs(r, c, node, word):
            # Base cases: out of bounds, already visited, or char not in Trie
            if r<0 or c<0 or r >= ROWS or c >= COLS or (r,c) in visit or board[r][c] not in node.children:
                return
            
            # Mark current cell as visited
            visit.add((r,c))

            # Move to next Trie node and build word
            node = node.children[board[r][c]]
            word += board[r][c]

            # Found a complete word!
            if node.endOfWord == True:
                res.add(word)

            # Explore all 4 directions
            dfs(r+1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c-1, node, word)

            # Backtrack: unmark cell so other paths can use it
            visit.remove((r,c))

        # Step 2: Start DFS from every cell on the board
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

            
