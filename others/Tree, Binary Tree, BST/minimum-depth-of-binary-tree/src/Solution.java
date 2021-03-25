/**
 * Minimum Depth of Binary Tree
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    public int minDepth(TreeNode root) {

        // Corner case
        if (root == null) return 0;

        // Leaf node
        if (root.left == null && root.right == null) return 1;

        int left = minDepth(root.left);
        int right = minDepth(root.right);

        // One side
        if (root.left == null || root.right == null) return left + right + 1;

        return Math.min(left, right) + 1;

    }
}