/**
 * <p>
 * 1448. Count Good Nodes in Binary Tree (Medium)
 * https://leetcode.com/problems/count-good-nodes-in-binary-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/30
 */
public class GoodNodes {

    private int res = 0;

    public int goodNodes(TreeNode root) {
        preorder(root, Integer.MIN_VALUE);
        return res;
    }


    public void preorder(TreeNode root, int max) {

        // Base case
        if (root == null) return;

        if (root.val >= max) {
            res++;
            max = root.val;
        }

        preorder(root.left, max);
        preorder(root.right, max);

    }

}
