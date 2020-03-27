/**
 * @Topic 70. Climbing Stairs
 * @Author Yi Cai
 * @Tag Dynamic Programming
 * @Date 3/21/2020 10:06 PM
 **/

class Solution {
    public int climbStairs(int n) {
        // corner case
        if (n == 0) return 0;
        if (n == 1) return 1;
        if (n == 2) return 2;
        int[] dp = new int[n + 1];  // dp[i] stands for the steps we need to climb i-th stairs
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        if (n < 3) return dp[n];
        for (int i = 3; i < dp.length; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}


// Time Complexity: O(n)
// Space Complexity: O(n)


/*
 * Study Notes:
 * Always remember the corner case!
 * */