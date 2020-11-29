/**
 * Climbing Stairs
 */
class Solution {

    // 1 <= n <= 45
    // dp[i]: how many ways to climb "i" steps
    private int[] dp = new int[46];

    public int climbStairs(int n) {

        // Base case
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];

    }
}