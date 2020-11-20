/**
 * Insert into a Binary Search Tree
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int val) {
            this.val = val;
        }
    }

    public TreeNode insertIntoBST(TreeNode root, int val) {

        if (root == null) return new TreeNode(val);

        // It's guaranteed that val does not exist in the original BST
        if (val < root.val) {
            root.left = insertIntoBST(root.left, val);
        } else {
            root.right = insertIntoBST(root.right, val);
        }

        return root;

    }
}