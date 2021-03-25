/**
 * <p>
 * 633. Sum of Square Numbers (Medium)
 * https://leetcode.com/problems/sum-of-square-numbers/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/3/24
 */
class SumOfSquareNumbers {
    public boolean judgeSquareSum(int c) {

        if (c == 0) return true;

        // head
        int i = 0;
        // tail
        int j = (int) Math.sqrt(c);
        int a, b = 0;

        /*
          1) a and b can be the same
          e.g: c = 2, 1^2 + 1^2 = 2

          2) including zero
          e.g: c = 4, 0^2 + 2^2 = 4
         */
        while (i <= j) {

            a = i * i;
            b = j * j;

            if (a + b == c) {
                // Bingo
                return true;
            } else if (a + b < c) {
                // Get larger
                i++;
            } else {
                // Get smaller
                j--;
            }
        }

        return false;

    }
}
