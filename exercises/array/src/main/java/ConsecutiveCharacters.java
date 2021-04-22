/**
 * <p>
 * 1446. Consecutive Characters (Easy)
 * Max Consecutive Ones 变式
 * https://leetcode.com/problems/consecutive-characters/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/22
 */
public class ConsecutiveCharacters {
    public int maxPower(String s) {

        int res = 0;
        char[] nums = s.toCharArray();
        int cnt = 0;
        char cmp = nums[0];

        for (char c : nums) {
            if (c == cmp) {
                cnt++;
            } else {
                // Keep tracking of "res"
                res = Math.max(cnt, res);
                // Restart
                cnt = 1;
                cmp = c;
            }
        }

        // Keep tracking of "res" (double check)
        return Math.max(cnt, res);

    }
}
