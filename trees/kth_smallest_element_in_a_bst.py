# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Solution 1: Iterative DFS (In-order Traversal)

# Intuition:
# 1. In-order traversal of a BST visits nodes in ascending sorted order (left -> root -> right)
# 2. We can use this property to find the kth smallest by counting nodes during traversal
# 3. Use a stack to simulate recursion iteratively, going as far left as possible first
# 4. When we process the kth node during in-order traversal, that's our answer

# Time Complexity: O(H + k) where H is the height of the tree
#   - In worst case (skewed tree), this becomes O(n) where n is total nodes
#   - We traverse down to the leftmost node (H steps), then process k nodes
# Space Complexity: O(H) for the stack, where H is the height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            # Phase 1: Go as far left as possible, pushing nodes onto stack
            # This finds the smallest unvisited element
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Phase 2: Process the current node (in-order position)
            curr = stack.pop()
            k -= 1  # Decrement k as we've visited one more node in sorted order
            
            # If we've visited k nodes, current node is the kth smallest
            if k == 0:
                return curr.val
            
            # Phase 3: Move to right subtree to continue in-order traversal
            curr = curr.right

# Solution 2: Recursive DFS (In-order Traversal)

# Intuition:
# 1. In-order traversal of a BST visits nodes in ascending sorted order (left -> root -> right)
# 2. We can count nodes as we visit them during in-order traversal
# 3. When count reaches k, we've found the kth smallest element
# 4. Use nonlocal variables to maintain state across recursive calls

# Time Complexity: O(H + k) where H is the height of the tree
#   - We traverse to the leftmost node (H steps), then process k nodes
#   - Worst case (skewed tree): O(n) where n is total nodes
#   - Best case (balanced tree): O(log n + k)
# Space Complexity: O(H) for the recursion call stack
#   - Worst case (skewed tree): O(n)
#   - Best case (balanced tree): O(log n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = root.val

        def inorder(node):
            nonlocal res, count
            
            # Base case: reached a null node
            if not node:
                return
            
            # Step 1: Recursively traverse left subtree (smaller elements)
            inorder(node.left)
            
            # Step 2: Process current node (in sorted order)
            count += 1
            if count == k:
                res = node.val  # Found the kth smallest element
                return  # Early termination - no need to continue
            
            # Step 3: Recursively traverse right subtree (larger elements)
            inorder(node.right)

        inorder(root)
        return res


# TODO: Figure out Morris Traversal for O(1) space