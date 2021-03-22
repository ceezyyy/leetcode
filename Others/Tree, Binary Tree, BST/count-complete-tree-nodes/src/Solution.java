/**
 * Count Complete Tree Nodes
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    public int countNodes(TreeNode root) {

        // Corner case
        if (root == null) return 0;

        return countNodes(root.left) + countNodes(root.right) + 1;

    }
}