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
    // 解法一: 常规两数相加
//    public int[] plusOne(int[] digits) {
//
//        // 1 <= digits.length <= 100
//        int n = digits.length;
//        int sum = 0;
//        int i = n - 1;
//
//        // last "bit"
//        sum = digits[i] + 1;
//        digits[i] = sum % 10;
//        sum /= 10;
//        i--;
//
//        while (sum > 0 && i >= 0) {
//            sum += digits[i];
//            digits[i] = sum % 10;
//            sum /= 10;
//            i--;
//        }
//
//        if (sum == 1) {
//            int[] res = new int[n + 1];
//            res[0] = 1;
//            for (int j = 1; j < n + 1; j++) {
//                res[j] = digits[j - 1];
//            }
//            return res;
//        }
//
//        return digits;
//
//    }

    // 解法二: 巧妙利用了只加 "1" 这个特性
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
