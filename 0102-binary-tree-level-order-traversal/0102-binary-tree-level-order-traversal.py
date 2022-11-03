# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = []
        
        queue.append(root)
        
        sol = []
        
        
        while queue:
            currArray = []
            curSubarray = []
            while queue:
                currArray.append(queue.pop(0))
            
            for n in currArray:
                curSubarray.append(n.val)
                
                if n.left:
                    queue.append(n.left)
                
                if n.right:
                    queue.append(n.right)
            
            sol.append(curSubarray)
        
        return sol