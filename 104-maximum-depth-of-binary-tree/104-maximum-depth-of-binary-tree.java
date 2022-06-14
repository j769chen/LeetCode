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
    public int dfs(TreeNode root) {
        if (root.left == null && root.right == null) {
            return 1;
        } 

        if (root.left == null) {
            return dfs(root.right) + 1;
        }
        else if (root.right == null) {
            return dfs(root.left)+ 1;        
        }
        else {
         return Math.max(dfs(root.right), dfs(root.left)) + 1;   
        }
    }
    
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        return dfs(root);
    }
}