# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        res = deque([root])

        def hazza(node, currDepth):
            if not node:
                return currDepth
            else:
                currDepth += 1
                return max(hazza(node.right, currDepth), hazza(node.left, currDepth))
       
        while res:
            currentNode = res.popleft()

            if abs(hazza(currentNode.left, 0) - hazza(currentNode.right, 0))> 1:
                return False

            if currentNode.left:
                res.append(currentNode.left)
            if currentNode.right:
                res.append(currentNode.right)
        return True
        












   
