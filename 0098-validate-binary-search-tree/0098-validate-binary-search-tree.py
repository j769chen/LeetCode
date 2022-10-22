# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTHelper(root, minVal, maxVal):
            if root is None:
                return True
            if root.val <= minVal or root.val >= maxVal:
                return False
            
            return isValidBSTHelper(root.left, minVal, root.val) and isValidBSTHelper(root.right, root.val, maxVal)
            
        
        return isValidBSTHelper(root, float('-inf'), float('inf'))