/**
 * <p>
 * 169. Majority Element (Easy)
 * Moore-Voting Algorithm
 * https://leetcode.com/problems/majority-element/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/22
 */
public class MajorityElement {
    public int majorityElement(int[] nums) {

        int n = nums.length;
        // Init
        int cand = nums[0];
        int cnt = 1;

        for (int i = 1; i < n; i++) {
            if (cnt == 0) {
                // Change candidate
                cand = nums[i];
                cnt = 1;
                continue;
            }
            cnt = nums[i] == cand ? cnt + 1 : cnt - 1;
        }

        return cand;

    }
}
