/**
 * <p>
 * 100. Same Tree (Easy)
 * https://leetcode.com/problems/same-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/30
 */
public class IsSameTree {
    public boolean isSameTree(TreeNode p, TreeNode q) {

        /*
          Preorder traversal
         */
        if (p == null && q == null) return true;

        if (p != null && q != null && p.val != q.val) return false;

        if (p == null || q == null) return false;

        return isSameTree(p.left == null ? null : p.left, q.left == null ? null : q.left)
                && isSameTree(p.right == null ? null : p.right, q.right == null ? null : q.right);

    }
}
