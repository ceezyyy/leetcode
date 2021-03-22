/**
 * Symmetric Tree
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    public boolean isSymmetric(TreeNode root) {
        return isMirror(root, root);
    }

    // Top-down
    public boolean isMirror(TreeNode n1, TreeNode n2) {
        // Corner cases
        if (n1 == null && n2 == null) return true;
        if (n1 == null || n2 == null) return false;

        return (n1.val == n2.val) && isMirror(n1.left, n2.right) && isMirror(n1.right, n2.left);
    }

}
