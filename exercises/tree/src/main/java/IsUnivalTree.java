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

        return traverse(root);

    }

    public boolean traverse(TreeNode root) {

        if (root == null) return true;

        /*
          Preorder traversal
         */
        if (root.val != uniqueVal) return false;

        return traverse(root.left) && traverse(root.right);

    }
}
