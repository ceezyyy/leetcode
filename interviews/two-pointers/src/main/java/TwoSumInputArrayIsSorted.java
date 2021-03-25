/**
 * <p>
 * 167. Two Sum II - Input array is sorted (Easy)
 * https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/24
 */
class TwoSumInputArrayIsSorted {
    public int[] twoSum(int[] nums, int target) {

        int[] res = new int[2];
        // head
        int i = 0;
        // tail
        int j = nums.length - 1;
        int a, b = 0;

        while (i < j) {

            a = nums[i];
            b = nums[j];

            if (a + b == target) {
                // Bingo
                res[0] = i + 1;
                res[1] = j + 1;
                return res;
            } else if (a + b > target) {
                // Get smaller
                j--;
            } else {
                // Get larger
                i++;
            }

        }

        return res;

    }
}
