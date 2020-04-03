/**
 * @Topic 643. Maximum Average Subarray I
 * @Author Yi Cai
 * @Tag Sliding Window
 * @Date 4/3/2020 10:50 PM
 **/


class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int left = 0;
        int right = k - 1;
        double currentSum = 0;
        double result = 0;

        // First k elements
        for (int i = 0; i < k; i++) {
            currentSum += nums[i];
        }
        result = currentSum;

        // Sliding Window
        while (right + 1 < nums.length) {
            right++;
            currentSum += nums[right] - nums[left];
            result = Math.max(currentSum, result);
            left++;
        }

        return result / k;
    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)

