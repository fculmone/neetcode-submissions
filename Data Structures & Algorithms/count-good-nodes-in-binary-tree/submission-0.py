# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_node_count = 0
        def dfs(root, max_above):
            if root is None:
                return
            if root.val >= max_above:
                nonlocal good_node_count
                good_node_count += 1 
                max_above = root.val
            dfs(root.left, max_above)
            dfs(root.right, max_above)

        dfs(root, float('-inf')) 
        return good_node_count