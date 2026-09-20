# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #bfs check for every node
    
        #bfsintolist
        
        def bfs(root):
            subList = []

            res = deque([root])

            while res:
                currentNode = res.popleft()

                subList.append(currentNode.val)

                if currentNode.left:
                    res.append(currentNode.left)
                if currentNode.right:
                    res.append(currentNode.right)
            return subList

        subList = bfs(subRoot)

        main = deque([root])
        
        while main:
            curr = main.popleft()

            if bfs(curr) == subList:
                return True
            
            if curr.left:
                main.append(curr.left)
            if curr.right:
                main.append(curr.right)

        return False







