/**
 * @Topic 633. Sum of Square Numbers
 * @Author Yi Cai
 * @Tag Two Pointers
 * @Date 3/28/2020 10:20 PM
 **/


class Solution {
    public boolean judgeSquareSum(int c) {
        // Two pointers
        int left = 0;
        int right = (int) Math.sqrt(c);  // The key of this topic
        while (left <= right) {
            int result = left * left + right * right;
            if (result == c) {
                return true;
            } else if (result < c) {
                left++;
            } else {
                right--;
            }
        }
        return false;
    }
}


// Time Complexity: O(sqrt(n))
// Space Complexity: O(1)

