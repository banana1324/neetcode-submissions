# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def isGood(root,maxSoFar):
            if root.val >= maxSoFar:
                nonlocal res
                res += 1
                #print(root.val, " ", maxSoFar)

                maxSoFar = root.val

            if root.left:
                isGood(root.left, maxSoFar)
            if root.right:
                isGood(root.right, maxSoFar)

            return
        
        isGood(root, root.val)
        return res
        