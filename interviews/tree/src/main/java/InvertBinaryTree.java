/**
 * <p>
 * 226. Invert Binary Tree (Easy)
 * https://leetcode.com/problems/invert-binary-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/24
 */
class InvertBinaryTree {
    public TreeNode invertTree(TreeNode root) {

        if (root == null) return root;

        /*
          For each node:

          1) invert its left & right child
          2) the left / right pointer points to the "invertedRight" / "invertedLeft"
         */
        TreeNode invertedLeft = invertTree(root.left);
        TreeNode invertedRight = invertTree(root.right);

        root.left = invertedRight;
        root.right = invertedLeft;

        return root;

    }
}
