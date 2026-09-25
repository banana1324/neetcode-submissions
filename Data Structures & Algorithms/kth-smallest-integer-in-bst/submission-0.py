# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        que = deque([root])
        vals = []

        while que:
            curr = que.popleft()

            vals. append(curr.val)

            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
        
        vals = sorted(vals)

        for x in range(len(vals)):
            if x == k -1:
                return vals[x]
        