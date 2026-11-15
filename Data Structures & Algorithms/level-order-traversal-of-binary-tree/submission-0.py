# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def bfs(root):
            queue = deque([root] if root is not None else [])
            while queue:
                curr_level = []
                for _ in range(len(queue)):
                    node = queue.popleft()
                    curr_level.append(node.val)
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:            
                        queue.append(node.right)
                result.append(curr_level)
        
        bfs(root)
        return result
