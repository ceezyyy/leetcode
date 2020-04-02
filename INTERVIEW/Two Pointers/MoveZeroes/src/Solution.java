/**
 * @Topic 283. Move Zeroes
 * @Author Yi Cai
 * @Tag Two Pointers
 * @Date 4/2/2020 9:30 AM
 **/


class Solution {
    public void moveZeroes(int[] nums) {
        // Slow pointer
        int slow = 0;

        // Fast pointer
        for (int fast = 0; fast < nums.length; fast++) {
            if (nums[fast] != 0) {
                nums[slow++] = nums[fast];
            }
        }

        // Set zeros
        for (int i = slow; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
}


// Time Complexity: O(n)
// Space Complexity: O(1)

