/**
 * <p>
 * 110. Balanced Binary Tree (Easy)
 * https://leetcode.com/problems/balanced-binary-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/24
 */
class BalancedBinaryTree {

    private boolean res = true;

    public boolean isBalanced(TreeNode root) {
        getHeight(root);
        return res;
    }

    public int getHeight(TreeNode root) {

        if (root == null) return 0;

        /*
          For each node:

          1) Get the depth of left and right child

          2) Determine whether the height of left / right child
             is no more than 1
         */
        int left = getHeight(root.left);
        int right = getHeight(root.right);

        if (Math.abs(left - right) > 1) res = false;

        return Math.max(left, right) + 1;

    }

}


/**
 * References:
 * https://www.youtube.com/watch?v=LU4fGD-fgJQ
 */
