# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        pFound = False
        qFound = False

        def findPath(root,num):
            path = []

            while root:
                path.append(root.val)

                if root.val == num.val:
                    return path
                elif root.val > num.val:
                    root = root.left
                else:
                    root = root.right
            return path
        ppath = findPath(root,p)
        qpath = findPath(root,q)
            
        print (ppath)
        print(qpath)
        for x in range(len(ppath)-1 , -1, -1):
            if ppath[x] in qpath:
                return TreeNode(ppath[x])
        
            