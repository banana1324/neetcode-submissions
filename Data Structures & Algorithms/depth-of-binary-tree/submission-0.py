# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def hazza(node, currDepth):
            if not node:
                return currDepth
            else:
                currDepth += 1
                return max(hazza(node.right, currDepth), hazza(node.left, currDepth))
        
        return hazza(root, 0)
            