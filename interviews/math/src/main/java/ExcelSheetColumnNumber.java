/**
 * <p>
 * 171. Excel Sheet Column Number (Easy)
 * https://leetcode.com/problems/excel-sheet-column-number/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/22
 */
public class ExcelSheetColumnNumber {
    public int titleToNumber(String columnTitle) {

        String s = new StringBuilder(columnTitle).reverse().toString();
        char[] nums = s.toCharArray();
        int n = nums.length;
        int res = 0;

        for (int i = 0; i < n; i++) {
            int cur = nums[i] - 'A' + 1;
            // 26-Base
            res += cur * (int) Math.pow(26, i);
        }

        return res;

    }
}
