# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced_height(node):
            if node is None:
                return (0, True)
                
            left = is_balanced_height(node.left)
            right = is_balanced_height(node.right)

            height = max(left[0] + 1, right[0] + 1)
            is_balanced = left[1] and right[1] and (abs(left[0] - right[0]) <= 1)
            return (height, is_balanced) 
        return is_balanced_height(root)[1]
        