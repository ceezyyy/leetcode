/**
 * @Topic 680. Valid Palindrome II
 * @Author Yi Cai
 * @Tag Two Pointers
 * @Date 3/29/2020 6:45 PM
 **/


class Solution {
    public boolean validPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left <= right) {
            if (s.charAt(left) != s.charAt(right)) {
                return isPalindrome(s, left + 1, right) || isPalindrome(s, left, right - 1);
            } else {
                left++;
                right--;
            }
        }
        return true;
    }

    private boolean isPalindrome(String s, int left, int right) {
        while (left <= right) {
            if (s.charAt(left++) != s.charAt(right--)) {
                return false;
            }
        }
        return true;
    }
}


// Time Complexity: O(n)
// Space Complexity: O(n)

