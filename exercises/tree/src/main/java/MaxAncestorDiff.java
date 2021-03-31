/**
 * <p>
 * 1026. Maximum Difference Between Node and Ancestor (Medium)
 * https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/31
 */
public class MaxAncestorDiff {

    private int res = 0;

    public int maxAncestorDiff(TreeNode root) {

        if (root == null) return 0;

        preorder(root, root.val, root.val);

        return res;

    }

    public void preorder(TreeNode root, int minVal, int maxVal) {

        if (root == null) return;

        minVal = Math.min(minVal, root.val);
        maxVal = Math.max(maxVal, root.val);
        res = Math.max(res, Math.abs(maxVal - minVal));

        preorder(root.left, minVal, maxVal);
        preorder(root.right, minVal, maxVal);

    }
}
