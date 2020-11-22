/**
 * Flatten Binary Tree to Linked List
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }

    private TreeNode tail = null;

    public void flatten(TreeNode root) {

        // Corner case
        if (root == null) return;

        TreeNode left = root.left;
        TreeNode right = root.right;

        flatten(left);
        flatten(right);

        root.left = null;
        root.right = left;

        // "left" may be null, to avoid NullPointerException
        // We need a cursor to reach the tail of the linked list
        tail = root;
        while (tail.right != null) tail = tail.right;

        // Now at the tail of the linked list
        tail.right = right;

    }
}