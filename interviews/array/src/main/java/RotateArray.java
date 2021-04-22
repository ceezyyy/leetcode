/**
 * <p>
 * 189. Rotate Array (Medium)
 * https://leetcode.com/problems/rotate-array/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/18
 */
public class RotateArray {

    private int[] nums;
    private int n;

    public void rotate(int[] nums, int k) {

        this.nums = nums;
        this.n = nums.length;

        // k is non-negative
        k = k % n;

        reverse(0,  - 1);
        reverse(0, k - 1);
        reverse(k, n - 1);

    }

    public void reverse(int i, int j) {
        while (i < j) {
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
            i++;
            j--;
        }
    }
}
