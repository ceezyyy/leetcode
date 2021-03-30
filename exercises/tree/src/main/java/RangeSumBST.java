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

        traverse(root);

        return res;

    }

    /**
     * Preorder traversal
     *
     * @param root
     */
    public void traverse(TreeNode root) {

        if (root == null) return;

        int cur = root.val;

        /*
          Preorder traversal
         */
        if (cur >= low && cur <= high) {
            res += cur;
            traverse(root.left);
            traverse(root.right);
        } else if (cur < low) {
            traverse(root.right);
        } else {
            traverse(root.left);
        }

    }
}
