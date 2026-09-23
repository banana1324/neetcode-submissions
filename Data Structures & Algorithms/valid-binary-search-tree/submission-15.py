# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(root, s,l):


            if root.val <= s or root.val >= l:
                return False


            if root.left:
                if not isValid(root.left, s, root.val):
                    return False
                
            
            if root.right:
                if not isValid(root.right, root.val, l):
                    return False

            return True
        if isValid(root,-1000000000 , 1000000000  ) == False:
            return False
        else:
            return True

        