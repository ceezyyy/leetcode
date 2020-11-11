/**
 * Maximum Binary Tree
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public TreeNode constructMaximumBinaryTree(int[] nums) {
        // Corner case
        if (nums == null || nums.length == 0) return null;
        return constructMaximumBinaryTree(nums, 0, nums.length);
    }

    // [left, right) interval
    public TreeNode constructMaximumBinaryTree(int[] nums, int left, int right) {

        // Corner case
        if (left >= right) return null;

        // Recursively
        int indexOfMax = getIndexOfMax(nums, left, right);
        TreeNode root = new TreeNode(nums[indexOfMax]);
        root.left = constructMaximumBinaryTree(nums, left, indexOfMax);
        root.right = constructMaximumBinaryTree(nums, indexOfMax + 1, right);

        return root;

    }

    public int getIndexOfMax(int[] nums, int left, int right) {
        int index = left;
        for (int i = left + 1; i < right; i++) {
            if (nums[i] > nums[index]) {
                index = i;
            }
        }
        return index;
    }
}
