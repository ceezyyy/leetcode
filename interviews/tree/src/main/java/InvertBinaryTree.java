/**
 * <p>
 * 226. Invert Binary Tree
 * https://leetcode.com/problems/invert-binary-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/24
 */
class InvertBinaryTree {
    public TreeNode invertTree(TreeNode root) {

        if (root == null) return null;

        TreeNode originLeft = root.left;
        TreeNode originRight = root.right;

        /*
          For each node:

          1) left pointer to the "right"

          2) right pointer to the "left"

         */
        root.left = invertTree(originRight);
        root.right = invertTree(originLeft);

        return root;

    }
}
