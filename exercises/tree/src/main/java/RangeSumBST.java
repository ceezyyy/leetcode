/**
 * <p>
 * 938. Range Sum of BST (Easy)
 * https://leetcode.com/problems/range-sum-of-bst/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/30
 */
public class RangeSumBST {
    private int res = 0;
    private int low;
    private int high;

    public int rangeSumBST(TreeNode root, int low, int high) {

        if (root == null) return 0;
        this.low = low;
        this.high = high;

        preorder(root);

        return res;

    }

    public void preorder(TreeNode root) {

        if (root == null) return;

        int cur = root.val;

        if (cur >= low && cur <= high) {
            res += cur;
            preorder(root.left);
            preorder(root.right);
        } else if (cur < low) {
            preorder(root.right);
        } else {
            preorder(root.left);
        }

    }
}
