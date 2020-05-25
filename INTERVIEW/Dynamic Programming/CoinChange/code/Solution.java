import java.util.Arrays;

/**
 * @Topic 322. Coin Change
 * @Author Yi Cai
 * @Tag Dynamic Programming
 * @Date 4/1/2020 11:54 AM
 **/


class Solution {
    public int coinChange(int[] coins, int amount) {
        // Initialization of dp array
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;

        // DP processl
        for (int i = 0; i < dp.length; i++) {
            for (int coin : coins) {
                if (i - coin >= 0) {
                    dp[i] = Math.min(dp[i - coin] + 1, dp[i]);
                }
            }
        }

        // Return the result
        return dp[amount] > amount ? -1 : dp[amount];
    }
}


// Time Complexity: O(m*n)
// Space Complexity: O(n)

