import java.util.Arrays;

/**
 * <p>
 * 1099. 小于 K 的两数之和 (Easy)
 * Two Sum 变式
 * https://leetcode-cn.com/problems/two-sum-less-than-k/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/18
 */
class TwoSumLessThanK {

    private int res = -1;

    public int twoSumLessThanK(int[] nums, int k) {

        Arrays.sort(nums);
        int i = 0;
        int j = nums.length - 1;

        while (i < j) {

            int sum = nums[i] + nums[j];
            // Keep tracking of "res"
            if (sum < k) res = Math.max(sum, res);

            if (sum >= k) {
                j--;
            } else {
                i++;
            }

        }

        return res;

    }
}
