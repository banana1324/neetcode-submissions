# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
            
        def dfs(node):
            res = []
            if node.left:
                res.extend(dfs(node.left))
            res.append(node.val)
            if node.right:
                res.extend(dfs(node.right))
            return res
        return dfs(root)
            