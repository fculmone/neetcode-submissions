# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    """
    isSubtree finds the place where the root
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_subtree(root, subroot):
            if subroot is None or root is None:
                return subroot is None and root is None

            l = is_subtree(root.left, subroot.left)
            r = is_subtree(root.right, subroot.right)
            print(l, r)

            return root.val == subroot.val and l and r

        if root is None:
            return subRoot is None
        
        if root.val == subRoot.val:
            retval = is_subtree(root, subRoot)
            if retval:
                return retval

        l = self.isSubtree(root.left, subRoot)  
        r = self.isSubtree(root.right, subRoot)
        return l or r 
        

