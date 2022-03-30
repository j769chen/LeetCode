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
    public List<Integer> preorderTraversal(TreeNode root) {
        Stack<TreeNode> nodes = new Stack<>();
        List<Integer> returnVal = new ArrayList<>();
        
        if (root == null) {
            return returnVal;
        }
        
        nodes.push(root);
        
        while(!nodes.isEmpty()) {
            TreeNode curr = nodes.pop();
            returnVal.add(curr.val);
            
            if(curr.right != null) {
                nodes.push(curr.right);
            }
            
            if(curr.left != null) {
                nodes.push(curr.left);
            }
            
           
        }
        
        return returnVal;
    }
}