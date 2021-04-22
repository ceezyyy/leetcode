/**
 * <p>
 *
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/22
 */
public class MissingNumber {
    public int missingNumber(int[] nums) {

        int n = nums.length;
        int actual = 0;

        for (int num : nums) actual += num;
        // Gauss' Formula
        int expected = (1 + n) * n / 2;

        return expected - actual;

    }
}
