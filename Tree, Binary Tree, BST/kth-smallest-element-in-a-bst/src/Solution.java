import java.util.ArrayList;
import java.util.List;

/**
 * Kth Smallest Element in a BST
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

    }

    public List<Integer> elements = new ArrayList<>();

    public int kthSmallest(TreeNode root, int k) {
        // The number of elements of the BST is between 1 to 10^4
        inorder(root);
        // You may assume k is always valid, 1 ≤ k ≤ BST's total elements
        return elements.get(k - 1);
    }

    public void inorder(TreeNode root) {
        // Corner case
        if (root == null) {
            return;
        }
        inorder(root.left);
        elements.add(root.val);
        inorder(root.right);
    }
}