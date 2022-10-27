# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, target, lis):
            if root:
                if root == target:
                    return lis
            
                lis.append(root)
                
                if dfs(root.left, target, lis) or dfs(root.right, target, lis):
                    return lis
                
                lis.pop()
        
        pList = []
        dfs(root, p, pList)
        
        qList = []
        dfs(root, q, qList)
        
        if(q in pList):
            return q
        
        if(p in qList):
            return p
        
        pSet = frozenset(pList)
        intersection = [x for x in qList if x in pSet]
        
        return intersection[-1]