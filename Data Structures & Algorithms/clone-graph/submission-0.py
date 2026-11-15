"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy = {}
        visited = set()
        def dfs(node):
            if node is None or node.val in visited:
                return
            visited.add(node.val)
            if node.val not in copy:
                copy[node.val] = Node(node.val)
            for n in node.neighbors:
                if n.val in copy:
                    copy[node.val].neighbors.append(copy[n.val])
                else:
                    copy[n.val] = Node(n.val)
                    copy[node.val].neighbors.append(copy[n.val])
                dfs(n)
        
        if node is None:
            return None
        dfs(node)
        return copy[node.val] 

        
         