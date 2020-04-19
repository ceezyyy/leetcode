/**
 * @Topic 485. Max Consecutive Ones
 * @Author Yi Cai
 * @Tag Array
 * @Date 4/7/2020 12:05 PM
 **/


class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int result = 0;
        int currentLength = 0;
        for (int num : nums) {
            if (num == 1) {
                currentLength += 1;
                result = Math.max(currentLength, result);
            } else {
                currentLength = 0;
            }
        }
        return result;
    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)

