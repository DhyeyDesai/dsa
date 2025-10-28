# Root to Leaf Paths
# https://bit.ly/3QA600D


"""
definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""


class Solution:
    def Paths(self, root):
        result = []

        # Perform DFS
        def dfs( node, result, path ):

            # Return nothing if the node is null
            if node is None:
                return
            
            # Append the node value to the current path.
            path.append(node.data)

            # If no left and right nodes are present, it means we have reached the end of the current path.
            # So append a copy of the path array to the result array.
            if not node.left and not node.right:
                result.append(path[:])

            # Otherwise, continue the recursion in current path on left and right nodes.
            # Pass the copy of the path array to next recursion calls.
            else:
                dfs(node.left, result, path)
                dfs(node.right, result, path) 
             
             # Backtrack: Remove the last node before returning
            path.pop()
        dfs(root, result, [])
        return result
    


# Note: 
# Why path[:]?
# Lists in Python are mutable, so when you do path.append(root.data), it modifies the same list object across recursive calls.
# When you append path to result (result.append(path)), you're appending a reference to the same list.
# Further recursive calls modify path, which also affects the already stored references in result. 

# Why path.pop()?
# Since path is a mutable list, all recursive calls modify the same list reference. Without pop(), elements from one recursive call would incorrectly persist in other calls.
# By using path.pop(), we ensure that:
# We remove the last node from the path when returning from a recursive call.
# This way, when we move to another branch, the path remains correct.



