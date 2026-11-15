# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(root, lower, upper):
            if root is None:
                return True
            if not lower < root.val < upper:
                return False
            l = is_valid(root.left, lower, root.val)
            r = is_valid(root.right, root.val, upper)
            return l and r
        return is_valid(root, float('-inf'), float('inf'))