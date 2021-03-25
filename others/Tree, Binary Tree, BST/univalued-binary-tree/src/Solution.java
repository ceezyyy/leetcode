/**
 * Univalued Binary Tree
 * <p>
 * A binary tree is univalued if every node in the tree has the same value.
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    public boolean isUnivalTree(TreeNode root) {
        // The number of nodes in the given tree will be in the range [1, 100]
        return isUnivalTree(root, root.val);
    }

    public boolean isUnivalTree(TreeNode root, int val) {

        // Corner case
        if (root == null) return true;

        if (root.val != val) return false;

        return isUnivalTree(root.left, val) && isUnivalTree(root.right, val);

    }
}