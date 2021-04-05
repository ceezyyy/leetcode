/**
 * <p>
 * 1161. Maximum Level Sum of a Binary Tree (Medium)
 * https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/31
 */
public class MaxLevelSum {

    // The number of nodes in the tree is in the range [1, 10^4]
    private int[] res = new int[10000];
    private int maxDepth = 0;
    private int maxKey;
    private int maxVal;

    public int maxLevelSum(TreeNode root) {

        preorder(root, 1);

        /*
          Find maximum level sum
         */
        maxKey = 0;
        maxVal = res[0];
        for (int i = 1; i < maxDepth; i++) {
            if (res[i] > maxVal) {
                maxVal = res[i];
                maxKey = i;
            }
        }

        return maxKey + 1;

    }

    public void preorder(TreeNode root, int depth) {

        if (root == null) return;

         res[depth - 1] += root.val;
        maxDepth = Math.max(maxDepth, depth);

        preorder(root.left, depth + 1);
        preorder(root.right, depth + 1);

    }
}
