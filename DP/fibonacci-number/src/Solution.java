/**
 * Fibonacci Number
 */
class Solution {

    // 0 ≤ N ≤ 30
    private int[] dp = new int[31];

    public int fib(int N) {

        // Base case
        dp[0] = 0;
        dp[1] = 1;

        for (int i = 2; i <= N; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[N];

    }
}