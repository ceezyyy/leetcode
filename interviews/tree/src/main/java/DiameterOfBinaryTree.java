/**
 * <p>
 * 543. Diameter of Binary Tree (Easy)
 * https://leetcode.com/problems/diameter-of-binary-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/24
 */
class DiameterOfBinaryTree {

    private int res = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        getMaxDepth(root);
        return res;

    }

    public int getMaxDepth(TreeNode root) {

        if (root == null) return 0;

        /*
          For each node:

          1) Get the max depth of left & right child

          2) Keep tracking the max path, because the longest path
             may or may not pass through the root
         */
        int left = getMaxDepth(root.left);
        int right = getMaxDepth(root.right);

        if (left + right > res) res = left + right;

        return Math.max(left, right) + 1;

    }
}
