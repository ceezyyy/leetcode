/**
 * <p>
 * 189. Rotate Array (Medium)
 * https://leetcode.com/problems/rotate-array/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/18
 */
public class RotateArrayI {
    public void rotate(int[] nums, int k) {

        int n = nums.length;
        int[] res = new int[n];

        for (int i = 0; i < n; i++) {
            // old -> new (mapping)
            res[(i + k) % n] = nums[i];
        }

        for (int i = 0; i < n; i++) {
            nums[i] = res[i];
        }

    }
}
