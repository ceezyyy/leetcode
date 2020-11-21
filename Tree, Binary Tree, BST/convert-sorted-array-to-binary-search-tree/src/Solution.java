/**
 * Convert Sorted Array to Binary Search Tree
 */
class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int val) {
            this.val = val;
        }
    }

    public TreeNode sortedArrayToBST(int[] nums) {
        // Corner case
        if (nums == null) return null;
        return sortedArrayToBST(nums, 0, nums.length - 1);
    }

    public TreeNode sortedArrayToBST(int[] nums, int start, int end) {

        // Corner case
        if (start > end) return null;

        // e.g: [1,2,3]
        // start, end = 2
        int k = start + (end - start) / 2;

        TreeNode root = new TreeNode(nums[k]);
        root.left = sortedArrayToBST(nums, start, k - 1);
        root.right = sortedArrayToBST(nums, k + 1, end);

        return root;

    }
}