/**
 * <p>
 * 104. Maximum Depth of Binary Tree (Easy)
 * https://leetcode.com/problems/maximum-depth-of-binary-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/24
 */
class MaxDepth {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
