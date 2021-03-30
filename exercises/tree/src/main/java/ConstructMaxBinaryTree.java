/**
 * <p>
 * 654. Maximum Binary Tree (Easy)
 * https://leetcode.com/problems/maximum-binary-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/30
 */
public class ConstructMaxBinaryTree {

    private int[] nums;
    private int n;

    public TreeNode constructMaximumBinaryTree(int[] nums) {

        this.nums = nums;
        this.n = nums.length;

        return construct(0, n - 1);

    }


    public TreeNode construct(int left, int right) {

        // Base case
        if (left > right) return null;

        /*
          Preorder traversal

          1) find the maximum element in [left, right]
          2) construct a new node
          3) left & right
         */
        int max = nums[left];
        int k = left;
        for (int i = left + 1; i <= right; i++) {
            if (nums[i] > max) {
                max = nums[i];
                k = i;
            }
        }

        TreeNode newNode = new TreeNode(nums[k]);

        newNode.left = construct(left, k - 1);
        newNode.right = construct(k + 1, right);

        return newNode;

    }
}
