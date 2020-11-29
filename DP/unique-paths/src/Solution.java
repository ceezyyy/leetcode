/**
 * Unique Paths
 */
class Solution {

    // dp[i][j]: Unique paths from dp[0][0] to dp[i][j] 
    private int[][] dp;

    public int uniquePaths(int m, int n) {

        // Corner case
        if (m == 1 || n == 1) return 1;

        dp = new int[m][n];

        // Base case
        dp[0][0] = 0;
        dp[0][1] = 1;
        dp[1][0] = 1;

        // The robot can only move either down or right at any point in time 
        // First row
        for (int j = 2; j < n; j++) dp[0][j] = dp[0][j - 1];
        // First col
        for (int i = 2; i < m; i++) dp[i][0] = dp[i - 1][0];

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }

        return dp[m - 1][n - 1];

    }
}