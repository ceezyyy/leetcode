/**
 * <p>
 * 538. Convert BST to Greater Tree (Medium)
 * https://leetcode.com/problems/convert-bst-to-greater-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/3
 */
public class ConvertBST {

    private int sum = 0;

    public TreeNode convertBST(TreeNode root) {
        inorder(root);
        return root;
    }

    public void inorder(TreeNode root) {

        if (root == null) return;

        inorder(root.right);
        sum += root.val;
        root.val = sum;
        inorder(root.left);

    }
}
