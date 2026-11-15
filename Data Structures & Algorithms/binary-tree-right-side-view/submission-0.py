# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_order = []
        right_view = []
        def bfs(root):
            queue = deque([root] if root is not None else [])
            while queue:
                last = None
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    last = node
                right_view.append(last.val)
        bfs(root)
        return right_view