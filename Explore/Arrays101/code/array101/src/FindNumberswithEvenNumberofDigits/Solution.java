package FindNumberswithEvenNumberofDigits;

/**
 * 1295. Find Numbers with Even Number of Digits
 * https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
 * Easy
 *
 * @author ceezyyy
 */
class Solution {
    public int findNumbers(int[] nums) {
        int result = 0;
        for (int i = 0; i < nums.length; i++) {
            // even digit
            if (countDigit(nums[i]) % 2 == 0) {
                result++;
            }
        }
        return result;
    }


    // number of digits
    public int countDigit(int num) {
        int digit = 1;
        while ((num / 10) != 0) {
            num /= 10;
            digit++;
        }
        return digit;
    }
}


