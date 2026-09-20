# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
                    
        level = deque([[root]])
        output = []


        while level:

            levelNodes = level.popleft()
            levelVals = []
            nextLevel = []
            for node in levelNodes:
                levelVals.append(node.val)

                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            output.append(levelVals)
            if nextLevel:
                level.append(nextLevel)

        return output




            
        