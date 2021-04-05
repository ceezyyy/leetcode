/**
 * <p>
 * 230. Kth Smallest Element in a BST (Medium)
 * https://leetcode.com/problems/kth-smallest-element-in-a-bst/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/3
 */
public class KthSmallest {

    private int res = 0;
    private int counter = 0;
    private int k = 0;

    public int kthSmallest(TreeNode root, int k) {
        this.k = k;
        inorder(root);
        return res;
    }

    public void inorder(TreeNode root) {

        if (root == null) return;

        inorder(root.left);
        counter++;
        if (counter == k) {
            res = root.val;
            return;
        }
        inorder(root.right);

    }
}
