/**
 * Path Sum
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    public boolean hasPathSum(TreeNode root, int sum) {

        // Corner case
        if (root == null) return false;

        // Leaf
        if (root.left == null && root.right == null && sum == root.val) {
            return true;
        }

        return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);

    }
}
