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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> vals = new ArrayList<Integer>();
        
        TreeNode curr = root;
        
        DFS(curr, vals);
        
        return vals;
    }
    
    public void DFS(TreeNode node, List<Integer> list) {
        
        if (node == null) {
            return;
        }
        
   
        DFS(node.left, list);
        list.add(node.val);
        DFS(node.right, list);
        
        
    }
}