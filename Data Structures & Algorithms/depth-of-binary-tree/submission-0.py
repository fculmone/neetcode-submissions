# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def max_depth_wrapper(root: Optional[TreeNode], depth: int) -> int:
            nonlocal max_depth
            if root is None:
                max_depth = max(max_depth, depth)
                return
            max_depth_wrapper(root.left, depth + 1) 
            max_depth_wrapper(root.right, depth + 1) 
        max_depth_wrapper(root, 0)
        return max_depth 