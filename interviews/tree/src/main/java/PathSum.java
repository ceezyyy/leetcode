/**
 * <p>
 * 112. Path Sum (Easy)
 * https://leetcode.com/problems/path-sum/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/29
 */
public class PathSum {
    public boolean hasPathSum(TreeNode root, int target) {

        // root-to-leaf path
        // e.g: [1, null, 2, null, 3] -> path sum: 6
        if (root == null) return false;

        // leaf
        if (root.left == null && root.right == null && root.val == target) return true;

        // If current node is not a leaf
        return hasPathSum(root.left, target - root.val) || hasPathSum(root.right, target - root.val);

    }
}
