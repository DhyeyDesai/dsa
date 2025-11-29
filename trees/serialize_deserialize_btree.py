# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/


# INTUITION:
# - We use preorder traversal (root -> left -> right) for both serialization and deserialization
# - During serialization, we represent null nodes as 'N' to maintain tree structure information
# - The key insight: preorder traversal naturally encodes parent-child relationships through ordering
# - During deserialization, we reconstruct the tree in the same preorder sequence, using an index
#   to track our position in the serialized string
# - When we encounter 'N', we know that subtree is null and can backtrack
# - This approach ensures we can uniquely reconstruct any binary tree structure

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node):
            # Base case: if node is null, append 'N' to mark null position
            if node is None:
                res.append('N')
                return
            
            # Preorder: process current node first
            res.append(str(node.val))
            
            # Recursively serialize left subtree
            dfs(node.left)
            
            # Recursively serialize right subtree
            dfs(node.right)
        
        # Start DFS from root
        dfs(root)
        
        # Join all values with commas to create serialized string
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        # Split the serialized string back into individual values
        vals = data.split(",")
        
        # Use instance variable to track current position in vals array
        # (allows us to maintain state across recursive calls)
        self.i = 0
        def dfs():
            # Base case: if current value is 'N', this position is null
            if vals[self.i] == "N":
                self.i+=1 # Move to next position
                return None
            
            # Create node with current value
            node = TreeNode(int(vals[self.i]))
            self.i += 1  # Move to next position for children
            
            # Recursively build left subtree (next values belong to left)
            node.left = dfs()
            
            # Recursively build right subtree (remaining values belong to right)
            node.right = dfs()

            return node
        
        # Start reconstruction from the beginning of vals array
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))