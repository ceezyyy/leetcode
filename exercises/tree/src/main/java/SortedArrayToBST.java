/**
 * <p>
 * 108. Convert Sorted Array to Binary Search Tree (Easy)
 * https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/30
 */
public class SortedArrayToBST {

    private int[] nums;

    public TreeNode sortedArrayToBST(int[] nums) {
        this.nums = nums;
        return traverse(0, nums.length - 1);
    }

    public TreeNode traverse(int left, int right) {

        // Base case
        if (left > right) return null;

        /*
          Preorder traversal
         */
        int mid = left + (right - left) / 2;
        TreeNode newNode = new TreeNode(nums[mid]);

        newNode.left = traverse(left, mid - 1);
        newNode.right = traverse(mid + 1, right);

        return newNode;

    }
}
