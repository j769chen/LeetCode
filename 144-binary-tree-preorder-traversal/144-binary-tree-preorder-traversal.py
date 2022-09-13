# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        lst = []
        stack = []
        if root is None:
            return lst
        stack.append(root)
        
        while(stack):
            s = stack.pop()
            
            lst.append(s.val)
            if(s.right is not None):
                stack.append(s.right)
            if(s.left is not None):
                stack.append(s.left)
        
        return lst