# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        lst = []
        stack = []
        cur = root
        
        while(len(stack) or cur):
            while(cur):
                stack.append(cur)
                cur = cur.left
            
            popped = stack.pop()
            lst.append(popped.val)
            cur = popped.right
        
        return lst