# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # root is always first elt of the preorder list
        root = TreeNode(preorder[0])

        # every elt to the left of the root in the inorder tree is on the left side of the tree, every elt to the right is on right side of tree
        rootIdx = inorder.index(preorder[0])
        
        # we know the size of each subtree based on the postiion of rootIdx, i.e. if theres one elt to the left of rootIdx in inorder,
        # then the first 1 elt in preorder is in the left subtree, same for right but everything after
        root.left = self.buildTree(preorder[1:rootIdx+1] ,inorder[:rootIdx])
        root.right = self.buildTree(preorder[rootIdx+1:], inorder[rootIdx+1:])
        
        return root