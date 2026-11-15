# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path1 = []
        path2 = []
        path1_vals = set()
        path2_vals = set()
        def build_path_to_node(root, path, path_vals, val):
            path.append(root)
            path_vals.add(root.val)

            if root.val == val:
                return
            elif val < root.val:
                build_path_to_node(root.left, path, path_vals, val)
            else:
                build_path_to_node(root.right, path, path_vals, val)
        
        # this is only run on q and checks when we get
        # off the path for path1
        def walk_to_node(root, val):
            if root.val == val:
                return root
            
            if val < root.val and root.left.val in path1_vals:
                return walk_to_node(root.left, val)
            elif val > root.val and root.right.val in path1_vals:
                return walk_to_node(root.right, val)
            else:
                return root

        print([x.val for x in path1])
        build_path_to_node(root, path1, path1_vals, p.val)
        return walk_to_node(root, q.val)
