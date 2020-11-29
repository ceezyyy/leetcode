/**
 * House Robber
 */
class Solution {

    // 0 <= nums.length <= 100
    // memo[i]: the maximum amount we can get before "i"
    private int[] memo = new int[101];

    public int rob(int[] nums) {

        // Corner case
        if (nums.length == 0) return 0;

        // Base case
        // "i-th" house: nums[i - 1]
        memo[0] = 0;
        memo[1] = nums[0];

        for (int i = 2; i <= nums.length; i++) {
            // Two choices: rob or not
            memo[i] = Math.max(memo[i - 2] + nums[i - 1], memo[i - 1]);
        }

        return memo[nums.length];

    }
}