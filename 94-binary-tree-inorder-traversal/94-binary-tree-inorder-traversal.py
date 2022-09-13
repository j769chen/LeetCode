# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            lst = []
            self.recursiveAdd(root,lst)
            return lst

    def recursiveAdd(self, root, lst):
            if root is not None:
                self.recursiveAdd(root.left, lst)
                lst.append(root.val)
                self.recursiveAdd(root.right, lst)