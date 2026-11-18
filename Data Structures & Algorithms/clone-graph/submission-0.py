"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        head = Node(1)
    
        def dfs(node):
            
            if not node:
                return node 

            if node in clones:
                return clones[node]

            new_node = Node(node.val)
            clones[node] = new_node

            for neighbor in node.neighbors:
                cloned_neighbor = dfs(neighbor)
                new_node.neighbors.append(cloned_neighbor)
            
            return new_node

        return dfs(node)