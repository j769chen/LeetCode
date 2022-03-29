/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean check(TreeNode q, TreeNode p) {
         
        
        if (q == null && p == null) {
            return true;
        }
        
        if (q == null || p == null) {
            return false;
        }
        
        if (q.val != p.val) {
            return false;
        }
        
        return true;
    }
    
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        
        Queue<TreeNode> leftTree = new LinkedList<>();
        Queue<TreeNode> rightTree = new LinkedList<>();
        
        leftTree.add(root.left);
        rightTree.add(root.right);
        
        while (!leftTree.isEmpty() && !rightTree.isEmpty()) {
            TreeNode left = leftTree.poll();
            TreeNode right = rightTree.poll();
            
            if(!check(left, right)) {
                return false;
            }
            
            if (left != null) {
                leftTree.add(left.left);
                leftTree.add(left.right);
            }
            
            if (right != null) {
                rightTree.add(right.right);
                rightTree.add(right.left);
            }
            
        }
        
        return true;
    }
}