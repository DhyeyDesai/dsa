# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Solution 1: Depth First Search (Not Optimal)

# Intuition:
# 1. Preorder traversal visits nodes as: Root -> Left -> Right
# 2. Inorder traversal visits nodes as: Left -> Root -> Right
# 3. First element in preorder is always the root of current subtree
# 4. Find this root in inorder to split left and right subtrees
# 5. Recursively build left subtree using elements before root in inorder
# 6. Recursively build right subtree using elements after root in inorder

# Time Complexity: O(n²) where n is the number of nodes
#   - We visit each node once: O(n)
#   - For each node, we call inorder.index() which is O(n)
#   - Array slicing creates new arrays: O(n) per recursive call
#   - Overall: O(n) * O(n) = O(n²)
# Space Complexity: O(n²) due to array slicing creating new subarrays
#   - Recursion call stack: O(h) where h is height
#   - Array slices at each level create copies: O(n) space per level
#   - Total across all recursive calls: O(n²)

# Note: This can be optimized to O(n) time and O(n) space using index pointers
# and a hashmap for inorder indices (see optimized solution)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: empty tree
        if not preorder or not inorder:
            return None
        
        # Step 1: First element in preorder is the root of current subtree
        root = TreeNode(preorder[0])
        
        # Step 2: Find root's position in inorder to determine left/right subtrees
        # Everything before mid in inorder belongs to left subtree
        # Everything after mid in inorder belongs to right subtree
        mid = inorder.index(preorder[0])

        # Step 3: Recursively build left subtree
        # preorder[1:mid+1] -> skip root, take next 'mid' elements (left subtree nodes)
        # inorder[:mid] -> all elements before root (left subtree nodes)
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        
        # Step 4: Recursively build right subtree
        # preorder[mid+1:] -> remaining elements after left subtree (right subtree nodes)
        # inorder[mid+1:] -> all elements after root (right subtree nodes)
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root


# Solution 2: Optimized DFS with Hashmap and Index Pointers

# Intuition:
# 1. Same logic as Solution 1, but avoid expensive array slicing and index() lookups
# 2. Use a hashmap to get inorder index of any value in O(1) time
# 3. Use index pointers (l, r) instead of creating new subarrays
# 4. Track current position in preorder with preIndex variable
# 5. Increment preIndex as we process each node in preorder sequence

# Time Complexity: O(n) where n is the number of nodes
#   - Building hashmap: O(n)
#   - Each node visited exactly once: O(n)
#   - Hashmap lookup for each node: O(1)
#   - No array slicing, just index arithmetic
# Space Complexity: O(n)
#   - Hashmap storing n elements: O(n)
#   - Recursion call stack: O(h) where h is height, worst case O(n)
#   - No additional space from array slicing

class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Build hashmap for O(1) lookup of index in inorder array
        # Key: node value, Value: index in inorder
        indices = {val: index for index, val in enumerate(inorder)}
        preIndex = 0  # Track current position in preorder array

        def dfs(l, r):
            nonlocal preIndex
            
            # Base case: invalid range means no subtree exists
            if l > r:
                return None
            
            # Step 1: Current preorder element is the root of this subtree
            nodeVal = preorder[preIndex]
            node = TreeNode(nodeVal)
            
            # Step 2: Find root's position in inorder using hashmap (O(1))
            mid = indices[nodeVal]
            
            # Step 3: Move to next element in preorder for next recursive call
            preIndex += 1

            # Step 4: Recursively build left subtree
            # Left subtree range: [l, mid-1] in inorder
            node.left = dfs(l, mid - 1)
            
            # Step 5: Recursively build right subtree
            # Right subtree range: [mid+1, r] in inorder
            node.right = dfs(mid + 1, r)
            
            return node
        
        # Start with full range of inorder array
        return dfs(0, len(inorder) - 1)


