/**
 * <p>
 * 125. Valid Palindrome (Easy)
 * https://leetcode.com/problems/valid-palindrome/
 * </p>
 *
 * @author ceezyyy
 * @since 2021/4/20
 */
public class ValidPalindrome {
    public boolean isPalindrome(String s) {

        char[] nums = s.toCharArray();
        int i = 0;
        int j = nums.length - 1;

        while (true) {

            while (i <= j && !Character.isLetterOrDigit(nums[i])) {
                i++;
            }
            while (i <= j && !Character.isLetterOrDigit(nums[j])) {
                j--;
            }

            // Failed cases
            if (i >= j) break;
            if (Character.toLowerCase(nums[i]) != Character.toLowerCase(nums[j])) return false;

            // Keep going
            i++;
            j--;

        }

        return true;

    }
}
