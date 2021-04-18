/**
 * <p>
 * 111. Minimum Depth of Binary Tree (Easy)
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/29
 */
public class MinDepth {
    public int minDepth(TreeNode root) {

        if (root == null) return 0;

        int leftDepth = minDepth(root.left);
        int rightDepth = minDepth(root.right);

        /*
          min path is from root to leaf
          so when we decide to choose a non-empty element between a and b
          we can just add them together ("a + b")
         */
        if (leftDepth == 0 || rightDepth == 0) return leftDepth + rightDepth + 1;

        return Math.min(leftDepth, rightDepth) + 1;

    }
}
