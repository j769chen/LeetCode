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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // p and q are both null
        if (p == null && q == null) return true;
        // one of p and q is null
        if (q == null || p == null) return false;
        
        Queue<TreeNode> nextP = new LinkedList<>();
        Queue<TreeNode> nextQ = new LinkedList<>();
        
        nextP.add(p);
        nextQ.add(q);
        
        while(!nextP.isEmpty()) {
            TreeNode currP = nextP.poll();
            TreeNode currQ = nextQ.poll();
            
            if ((currP == null && currQ != null) || (currP != null && currQ ==null)) {
                return false;
            }
            
            if ((currP != null && currQ != null) && currP.val != currQ.val ) {
                return false;
            }
            
            if(currP != null) {
                nextP.add(currP.left);
                nextP.add(currP.right);
            }
            
            if(currQ != null) {
                nextQ.add(currQ.left);
                nextQ.add(currQ.right);
            }
        }
        
        return true;
    }
}