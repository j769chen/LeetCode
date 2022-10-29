# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(curr, lis):
            if curr is None:
                return

            inorder(curr.left, lis)
            lis.append(curr.val)
            
            inorder(curr.right, lis)
        
        lis = []
        
        inorder(root, lis)
        
        return lis[k-1]
            