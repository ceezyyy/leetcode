/**
 * Convert BST to Greater Tree
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    private int sum = 0;

    public TreeNode convertBST(TreeNode root) {
        calculateBST(root);
        return root;
    }

    public void calculateBST(TreeNode root) {

        // Corner case
        if (root == null) return;

        calculateBST(root.right);
        // Key point
        sum += root.val;
        root.val = sum;
        calculateBST(root.left);

    }
}
