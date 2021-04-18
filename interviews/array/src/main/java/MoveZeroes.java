/**
 * <p>
 * 283. Move Zeroes (Easy)
 * https://leetcode.com/problems/move-zeroes/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/18
 */
public class MoveZeroes {
    public void moveZeroes(int[] nums) {

        // 1 <= nums.length <= 10^4
        int n = nums.length;

        int i = 0;

        // "j" should start from zero!
        for (int j = 0; j < n; j++) {
            if (nums[j] != 0) {
                nums[i] = nums[j];
                i++;
            }
        }

        // Filling w/ zero
        while (i < n) {
            nums[i] = 0;
            i++;
        }

    }
}
