# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def maxDepthHelper(count, root):
            if root == None:
                return count
            
            return max(maxDepthHelper(count+1, root.left), 
            maxDepthHelper(count+1,root.right))
        
        return maxDepthHelper(0, root)
        