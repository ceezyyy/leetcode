/**
 * <p>
 * 67. Add Binary (Easy)
 * https://leetcode.com/problems/add-binary/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/16
 */
public class AddBinary {
    public String addBinary(String a, String b) {

        StringBuilder res = new StringBuilder();
        /*
          1) Reverse
          Because we should starting from the smallest bit
         */
        StringBuilder sb1 = new StringBuilder(a).reverse();
        StringBuilder sb2 = new StringBuilder(b).reverse();
        int n1 = a.length();
        int n2 = b.length();
        int sum = 0;

        // 2) Fill in if necessary
        int diff = n1 - n2;
        if (diff < 0) {
            diff = -diff;
            while (diff-- > 0) {
                sb1.append('0');
            }
        }
        if (diff > 0) {
            while (diff-- > 0) {
                sb2.append('0');
            }
        }

        // 3) Add up
        for (int i = 0; i < Math.max(n1, n2); i++) {
            sum += sb1.charAt(i) - '0' + sb2.charAt(i) - '0';
            res.append(sum % 2);
            sum /= 2;
        }

        // 4) Fill in again if necessary
        if (sum == 1) res.append('1');
        return res.reverse().toString();

    }
}
