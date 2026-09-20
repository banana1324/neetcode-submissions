# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        #dfs

        def dfs(root):
            if not root.right and val > root.val:
                root.right = TreeNode(val)
                return 
            if not root.left and val < root.val:
                root.left = TreeNode(val)
                return 
            
            if val > root.val and root.right:
                return dfs(root.right)
            elif root.left:
                return dfs(root.left)
        dfs(root)
        return root

        
            
            