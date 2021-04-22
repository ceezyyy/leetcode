/**
 * <p>
 * 485. Max Consecutive Ones (Easy)
 * https://leetcode.com/problems/max-consecutive-ones/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/22
 */
public class MaxConsecutiveOnes {
    public int findMaxConsecutiveOnes(int[] nums) {

        int res = 0;
        int n = nums.length;
        int cnt = 0;

        for (int num : nums) {
            if (num == 1) {
                cnt++;
            } else {
                res = Math.max(cnt, res);
                cnt = 0;
            }
        }

        return Math.max(cnt, res);

    }
}
