/**
 * <p>
 * 26. Remove Duplicates from Sorted Array (Easy)
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/18
 */
public class RemoveDuplicates {
    public int removeDuplicates(int[] nums) {

        if (nums == null || nums.length == 0) return 0;
        int index = 0;
        int cmp = nums[0];
        int cur;

        for (int i = 1; i < nums.length; i++) {

            cur = nums[i];

            if (cur != cmp) {
                nums[++index] = cur;
                cmp = cur;
            }

        }

        return index + 1;

    }
}
