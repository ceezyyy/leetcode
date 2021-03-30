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
        traverse(root, Integer.MIN_VALUE);
        return res;
    }


    public void traverse(TreeNode root, int max) {

        // Base case
        if (root == null) return;

        /*
          Preorder traversal

          Keep tracking the maximum of each path
         */
        if (root.val >= max) {
            res++;
            max = root.val;
        }

        traverse(root.left, max);
        traverse(root.right, max);

    }

}
