# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def get_height(node):
            if node is None:
                return 0
            hl = get_height(node.left) + 1
            hr = get_height(node.right) + 1
            nonlocal diameter
            diameter = max(diameter, (hl - 1) + (hr - 1))
            return max(hl, hr)
        
        get_height(root)
        return diameter
        