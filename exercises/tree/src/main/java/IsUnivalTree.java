/**
 * <p>
 * 965. Univalued Binary Tree
 * https://leetcode.com/problems/univalued-binary-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/30
 */
public class IsUnivalTree {

    private int uniqueVal;

    public boolean isUnivalTree(TreeNode root) {

        if (root == null) return true;
        uniqueVal = root.val;

        return preorder(root);

    }

    public boolean preorder(TreeNode root) {

        if (root == null) return true;

        if (root.val != uniqueVal) return false;

        return preorder(root.left) && preorder(root.right);

    }
}
