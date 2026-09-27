# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        root = deque([root])

        que = deque([root])

        eachLev = []

        while que: #while there are still levels

            currLevel = que.popleft() #a deque of curr level
            nextLevel = deque()
            currList = []


            while currLevel:
                currNode = currLevel.popleft()
                currList.append(currNode.val)
                print(currNode.val)

                if currNode.left:
                    nextLevel.append(currNode.left)

                if currNode.right:
                    nextLevel.append(currNode.right)
            if nextLevel:
                que.append(nextLevel)

            eachLev.append(currList)

        res = []
        for level in eachLev:
            res.append(level[-1])
        return res
        


