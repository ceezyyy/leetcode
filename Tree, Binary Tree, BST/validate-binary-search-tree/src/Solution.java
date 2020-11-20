/**
 * Validate Binary Search Tree
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    public boolean isValidBST(TreeNode root) {

        // Corner case
        if (root == null) return true;

        // Use Long instead of Integer
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);

    }

    public boolean isValidBST(TreeNode root, long min, long max) {

        // Corner case
        if (root == null) return true;

        // Root: -inf < root < inf
        // Left subtree: -inf < left < root
        // Right subtree: root < right < inf
        int val = root.val;
        if (val >= max || val <= min) return false;

        return isValidBST(root.left, min, val) && isValidBST(root.right, val, max);

    }
}