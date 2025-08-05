# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if not root:
                return 0
            res = 1 if root.val>=maxVal else 0
            maxVal = max(root.val, maxVal)
            leftGood = dfs(root.left, maxVal)
            rightGood = dfs(root.right,maxVal)
            return leftGood+rightGood+res
        return dfs(root, root.val)