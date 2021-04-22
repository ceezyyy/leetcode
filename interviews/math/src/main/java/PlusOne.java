/**
 * <p>
 * 66. Plus One (Easy)
 * https://leetcode.com/problems/plus-one/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/18
 */
public class PlusOne {
    public int[] plusOne(int[] digits) {

        int n = digits.length;

        // Backwards
        for (int i = n - 1; i >= 0; i--) {

            // No carry
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }

            // Carry
            digits[i] = 0;

        }

        // Still not returned
        digits = new int[n + 1];
        digits[0] = 1;
        return digits;

    }

}
