/**
 * <p>
 * 1022. Sum of Root To Leaf Binary Numbers (Easy)
 * https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/30
 */
public class SumRootToLeaf {

    private int res = 0;

    public int sumRootToLeaf(TreeNode root) {

        if (root == null) return 0;

        StringBuilder init = new StringBuilder(String.valueOf(root.val));
        countPath(root.left, new StringBuilder(init));
        countPath(root.right, new StringBuilder(init));

        return res == 0 ? root.val : res;

    }

    /**
     * Count every root-to-leaf paths
     *
     * @param root
     * @param sb
     */
    public void countPath(TreeNode root, StringBuilder sb) {

        if (root == null) return;

        sb.append(String.valueOf(root.val));

        /*
          Won't stop until we meet leaf node
         */
        if (root.left == null && root.right == null) {
            // binary string -> int
            res += Integer.parseInt(sb.toString(), 2);
            return;
        }

        countPath(root.left, new StringBuilder(sb));
        countPath(root.right, new StringBuilder(sb));

    }
}
